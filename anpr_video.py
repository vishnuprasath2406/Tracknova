"""
TrackNova ANPR - reads number plates from a video with a real plate detector + OCR model.

Pipeline: YOLOv9 plate detector -> padded crop -> CCT OCR -> Indian plate format fix
          -> tracking -> per-character voting over many frames -> green box + final plate.

Setup (once):   pip install fast-alpr[onnx] opencv-python
Run:            python anpr_video.py traffic.mp4
Output:         traffic_anpr.mp4 (green boxes + plate text)  and  traffic_plates.json
"""
import sys, json, collections, cv2
from open_image_models import LicensePlateDetector
from fast_plate_ocr import LicensePlateRecognizer

STATES = set("AN AP AR AS BR CG CH DD DL DN GA GJ HP HR JH JK KA KL LA LD MH ML MN MP MZ NL OD OR PB PY RJ SK TN TR TS UK UP WB".split())
L2D = dict(O='0', Q='0', D='0', I='1', L='1', Z='2', S='5', B='8', G='6')
D2L = {'0': 'O', '1': 'I', '2': 'Z', '5': 'S', '8': 'B', '6': 'G'}


def fix_plate(raw):
    """Indian format: 2 letters + 2 digits + 1-3 letters + 4 digits. Fix O/0, I/1, S/5, B/8 by position."""
    s = ''.join(c for c in raw.upper() if c.isalnum())
    best = None
    for a in range(len(s)):
        for n in (9, 10, 11):
            t = s[a:a + n]
            if len(t) < n:
                continue
            out, c, ok = '', 0, True
            for i, ch in enumerate(t):
                digit = 2 <= i < 4 or i >= n - 4
                if digit and ch.isalpha():
                    if ch in L2D: ch, c = L2D[ch], c + 1
                    else: ok = False; break
                elif not digit and ch.isdigit():
                    if ch in D2L: ch, c = D2L[ch], c + 1
                    else: ok = False; break
                out += ch
            if ok and out[:2] in STATES and (best is None or c < best[1]):
                best = (out, c)
    return best[0] if best else None


def iou(a, b):
    x1, y1, x2, y2 = max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])
    i = max(0, x2 - x1) * max(0, y2 - y1)
    u = (a[2] - a[0]) * (a[3] - a[1]) + (b[2] - b[0]) * (b[3] - b[1]) - i
    return i / u if u else 0


def vote(reads):
    """Majority per character over raw reads of the most common length, then Indian-format correction."""
    if not reads: return None, 0.0
    n = collections.Counter(len(r) for r in reads).most_common(1)[0][0]
    same = [r for r in reads if len(r) == n]
    text = ''.join(collections.Counter(r[i] for r in same).most_common(1)[0][0] for i in range(n))
    fixed = fix_plate(text)
    if not fixed:                                   # fall back to the best single valid read
        valid = collections.Counter(f for f in map(fix_plate, reads) if f)
        fixed = valid.most_common(1)[0][0] if valid else None
    return fixed, len(same) / len(reads)


def main(src):
    det = LicensePlateDetector(detection_model="yolo-v9-t-384-license-plate-end2end")
    ocr = LicensePlateRecognizer("cct-xs-v2-global-model")
    cap = cv2.VideoCapture(src)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    W, H = int(cap.get(3)), int(cap.get(4))
    base = src.rsplit('.', 1)[0]
    out = cv2.VideoWriter(base + '_anpr.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (W, H))
    tracks, nxt, fr = [], 1, 0
    while True:
        ok, im = cap.read()
        if not ok: break
        fr += 1
        for t in tracks: t['miss'] += 1
        if fr % 2 == 0:                       # detect on every 2nd frame (speed); boxes persist in between
            reads_new = []
            for d in det.predict(im):
                b = d.bounding_box
                box = [b.x1, b.y1, b.x2, b.y2]
                w, h = box[2] - box[0], box[3] - box[1]
                if w < 24 or h < 8: continue          # too small to read
                for p in (.1, .25, .4):               # several paddings = several reads (edge characters get included)
                    c = im[max(0, int(box[1] - p * h)):int(box[3] + p * h), max(0, int(box[0] - p * w)):int(box[2] + p * w)]
                    c = cv2.resize(c, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
                    raw = ''.join(ch for ch in (ocr.run(c)[0].plate or '').upper() if ch.isalnum())
                    if 8 <= len(raw) <= 11: reads_new.append(raw)
                t = max(tracks, key=lambda t: iou(t['box'], box), default=None)
                if not t or iou(t['box'], box) < .2:
                    t = dict(id=nxt, reads=[], box=box, miss=0); nxt += 1; tracks.append(t)
                t['box'], t['miss'] = box, 0
                t['reads'] += reads_new; reads_new = []
        for t in tracks:
            if t['miss'] > fps * 1.5: continue
            text, share = vote(t['reads'])
            x1, y1, x2, y2 = map(int, t['box'])
            sure = len(t['reads']) >= 3 and text
            col = (0, 220, 0) if sure else (0, 200, 255)             # green = confirmed
            cv2.rectangle(im, (x1, y1), (x2, y2), col, 2)
            label = f"{text} {share*100:.0f}%" if sure else "reading..."
            (tw, th), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, .6, 2)
            cv2.rectangle(im, (x1, y1 - th - 10), (x1 + tw + 8, y1), (0, 0, 0), -1)
            cv2.putText(im, label, (x1 + 4, y1 - 6), cv2.FONT_HERSHEY_SIMPLEX, .6, col, 2)
        out.write(im)
    result = []
    for t in tracks:
        text, share = vote(t['reads'])
        if text and len(t['reads']) >= 3:
            result.append(dict(plate=text, agreement=round(share, 2), reads=len(t['reads'])))
    json.dump(result, open(base + '_plates.json', 'w'), indent=2)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main(sys.argv[1])

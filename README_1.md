<!-- Animated banner -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1668e3,100:7a6ff0&height=190&section=header&text=TrackNova&fontColor=ffffff&fontSize=62&fontAlignY=38&desc=Chennai%20Traffic%20Intelligence%20Platform&descAlignY=60&descSize=20" alt="TrackNova banner" width="100%"/>
</p>

<p align="center">
  <a href="https://vishnuprasath2406.github.io/Tracknova/">
    <img src="https://readme-typing-svg.demolab.com?font=Sora&weight=600&size=22&duration=3200&pause=900&color=1668E3&center=true&vCenter=true&width=720&lines=Multi-camera+ANPR+%26+vehicle+journey+tracking;Real-time+congestion+on+a+satellite+map;Rain-aware+routing+for+safer+commutes;Smart+city+analytics%2C+built+for+Chennai" alt="Typing animation" />
  </a>
</p>

<p align="center">
  <a href="https://vishnuprasath2406.github.io/Tracknova/"><img src="https://img.shields.io/badge/Live%20Demo-Open%20App-1668e3?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Live demo"/></a>
  <a href="https://github.com/vishnuprasath2406/Tracknova"><img src="https://img.shields.io/badge/Source-GitHub-0d1b2e?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>
  <img src="https://img.shields.io/badge/Status-Frontend%20Prototype-e5a100?style=for-the-badge" alt="Status"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white" alt="Leaflet"/>
  <img src="https://img.shields.io/badge/Tesseract.js-OCR-4c9bff?style=flat-square" alt="Tesseract.js"/>
  <img src="https://img.shields.io/badge/Open--Meteo-Weather%20API-3fb37f?style=flat-square" alt="Open-Meteo"/>
</p>

<p align="center">
  <img src="assets/live-traffic.gif" alt="TrackNova live traffic animation" width="88%"/>
</p>

---

## Table of Contents

- [About the Project](#about-the-project)
- [How It Works](#how-it-works)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Team](#team)
- [Credits and Acknowledgements](#credits-and-acknowledgements)
- [Roadmap](#roadmap)
- [Disclaimer](#disclaimer)

---

## About the Project

**TrackNova** is a city-wide AI traffic platform that combines multi-camera ANPR (Automatic Number Plate Recognition), real-time congestion monitoring, rainfall-aware routing and journey analytics into one dashboard. It is modelled on a 14-junction network across Chennai, from Parry's Corner and Marina Beach to Guindy, Velachery and Tidel Park.

The aim is simple: help traffic authorities see the whole city at once, and help citizens choose safer, faster routes.

> The current release is a **frontend-only prototype** driven by simulated traffic data. Plate recognition and rainfall detection, however, run on real inputs (an uploaded video and the Open-Meteo weather API).

---

## How It Works

<p align="center">
  <img src="assets/how-it-works.gif" alt="TrackNova processing pipeline" width="92%"/>
</p>

| Step | Stage | What happens |
|:---:|---|---|
| 01 | **Camera feeds** | Live CCTV and ANPR cameras at 14 junctions feed the system. |
| 02 | **ANPR / OCR** | Plates are read from video frames with Tesseract.js and checked against the Indian plate format. |
| 03 | **AI matching** | The same vehicle is matched across cameras and frames. |
| 04 | **Trajectory tracking** | A vehicle's path is rebuilt by time and location and replayed on a satellite map. |
| 05 | **Analytics dashboard** | Flow, density, congestion and travel time are visualised. |
| 06 | **Alerts and violations** | Flagged vehicles, incidents, heavy rain and camera outages raise notifications. |

---

## Key Features

### Traffic Intelligence
- **Dashboard**: live KPIs for vehicles, average speed, congestion index, active incidents and camera health, with a network map and hotspot list.
- **Live Traffic**: satellite map (Esri World Imagery) with colour-coded roads. Click any road or junction for speed, length and congestion.
- **Route Planner**: Dijkstra-based routing with *Fastest*, *Shortest*, *Least congested* and *Rain-safe* options, each with time, distance and rain exposure.

### ANPR and Vehicle Journeys
- **ANPR module**: upload a traffic video and plates are read frame by frame using OCR, with Indian format validation (state code, district, series, number) and common-misread correction.
- **Plate tracking**: a template tracker keeps the green plate box locked to the vehicle while it moves.
- **Vehicle Journey**: enter a plate number to replay its path across junctions, with per-leg road, speed, distance, timestamps and an animated vehicle on the satellite map.

### Rain Watch
- **Rainfall detection**: choose a *Demo storm* or *Live weather* (Open-Meteo, no API key needed) to see rain intensity per junction.
- **Rain-related accidents**: incidents linked to wet-road conditions are tagged and listed.
- **Rain-safe routing**: heavy-rain roads (7.5 mm/h and above) are avoided automatically, and slowdowns are included in travel times.

### Safety, Alerts and Control
- **Incident reporting** with status workflow (Reported, Investigating, Analyzing, Resolved).
- **Notifications** for heavy traffic, accidents, camera outages, flagged vehicles and heavy rain.
- **Admin console**: user management, camera on/off control, broadcast alerts, CSV exports (vehicles, incidents, congestion) and an audit log.
- **Analytics**: Today / 7 days / 30 days views with animated KPIs, clickable charts and per-junction filtering.

### Experience
- **AI Traffic Assistant**: a chat widget that answers traffic questions and navigates by command, such as "take me to analytics".
- **Multilingual interface**: English, Hindi and Tamil (plus Bengali labels).
- **Accessibility and theming**: adjustable text size, light and dark themes, responsive layout for phone and desktop.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Front end | HTML5, CSS3, vanilla JavaScript (single-page app) |
| Maps | [Leaflet 1.9.4](https://leafletjs.com/) with Esri World Imagery tiles, plus a built-in canvas map fallback |
| OCR | [Tesseract.js 5.1.1](https://github.com/naptha/tesseract.js) with a custom plate validator and tracker |
| Weather | [Open-Meteo](https://open-meteo.com/) precipitation API |
| Charts | Hand-built SVG line, bar, donut and bar-list charts |
| Storage and security | `localStorage` for sessions and audit log, Web Crypto SHA-256 for password hashing |
| Typography | Manrope and Sora (Google Fonts) |

---

## Getting Started

**Use it online:** open the [live demo](https://vishnuprasath2406.github.io/Tracknova/). No sign-in is required, as login is bypassed for demonstration.

**Run it locally:**

1. Download or clone the repository from GitHub.
2. Open `index.html` in any modern browser (Chrome, Edge or Firefox).
3. For the most reliable results, serve the folder with any simple local web server instead of opening the file directly.

**Try the ANPR module:** sign in as admin (demo mode does this automatically), open **ANPR**, click **Upload video**, choose a traffic clip and press play.

> An internet connection is needed for map tiles, fonts, Tesseract.js and live weather.

---

## Project Structure

| File / Folder | Purpose |
|---|---|
| `index.html` | Complete application: interface, logic and styles |
| `assets/` | README animations (`live-traffic.gif`, `how-it-works.gif`) |
| `README.md` | Project documentation |

---

## Team

<p align="center">
  <img src="https://img.shields.io/badge/Team-TrackNova-1668e3?style=for-the-badge" alt="Team TrackNova"/>
</p>

| | Name | Role | What they developed |
|:---:|---|---|---|
| 👑 | **VISHNU PRASATH S** | **Team Leader, Lead Developer and System Architect** | Overall architecture and project direction; the ANPR engine (OCR pipeline, Indian plate validation, frame-by-frame plate tracker); vehicle journey tracking; satellite map integration; Rain Watch and rain-safe routing; admin console; landing page and final integration. |
| 💻 | **JUPALLI DHARAN** | **Developer: Data and Analytics** | Analytics module (time-range views, filters, clickable charts, CSV export); incident reporting workflow; notifications system. |
| 🎨 | **VIJAYRAJ G** | **Developer: UI/UX and Frontend** | Interface design and theming (light and dark); responsive layout; settings and accessibility options; multilingual interface; profile page. |

---

## Credits and Acknowledgements

### 🏆 Special Credits: Team Leader

**VISHNU PRASATH S** conceived TrackNova, designed its architecture and led the team from idea to a working, deployed product. Beyond building the core ANPR, tracking, mapping and rain-intelligence modules, he guided the team throughout: planning the work, assigning responsibilities, reviewing contributions, resolving technical problems and bringing every module together into one consistent platform.

### Libraries and Services

- [Leaflet](https://leafletjs.com/) for interactive maps
- [Esri World Imagery](https://www.arcgis.com/) for satellite tiles
- [Tesseract.js](https://github.com/naptha/tesseract.js) for in-browser OCR
- [Open-Meteo](https://open-meteo.com/) for free weather data
- [Google Fonts](https://fonts.google.com/): Manrope and Sora
- [Shields.io](https://shields.io/), [Capsule Render](https://github.com/kyechan99/capsule-render) and [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) for this README

---

## Roadmap

- [ ] Java backend with REST APIs and a persistent database
- [ ] Server-side ANPR model (detector plus OCR) for production-grade accuracy
- [ ] Real CCTV and RTSP stream integration
- [ ] Cross-camera vehicle re-identification
- [ ] Stolen and blacklisted vehicle database integration
- [ ] Mobile app for citizens

---

## Disclaimer

TrackNova is an academic prototype. Traffic, congestion and most incident data are **simulated** for demonstration. Plate recognition accuracy depends on video quality and is not suitable for enforcement use. Login is intentionally disabled in the demo build.

---

<p align="center">
  <b>Built with ❤️ by Team TrackNova</b><br/>
  <sub>VISHNU PRASATH S · JUPALLI DHARAN · VIJAYRAJ G</sub>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7a6ff0,100:1668e3&height=110&section=footer" alt="footer" width="100%"/>
</p>

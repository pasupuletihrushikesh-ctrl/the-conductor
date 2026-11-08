# The Conductor — Central Orchestrator AI

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Theme: Maroon & Beige](https://img.shields.io/badge/Theme-Maroon_%26_Beige-722631.svg)](https://github.com/pasupuletihrushikesh-ctrl/the-conductor)
[![Python: FastAPI](https://img.shields.io/badge/Backend-FastAPI-009688.svg)](https://fastapi.tiangolo.com)
[![GitHub Pages](https://img.shields.io/badge/Live-GitHub_Pages-brightgreen.svg)](https://pasupuletihrushikesh-ctrl.github.io/the-conductor/)

**The Conductor** is an autonomous Central Orchestrator AI designed to analyze multi-phase projects, route requirements to specialized agents, manage seamless context handoffs, and emit frontend UI commands that drive smooth physical icon transitions within a **Maroon &amp; Beige interactive dashboard**.

---

## 🏛️ Multi-Agent Roster

| Agent | Icon | Core Capabilities |
| :--- | :---: | :--- |
| **Orchestrator** (The Conductor) | 🎻 | Master routing engine, milestone decomposition, cross-agent handoffs, UI trigger emission. |
| **Architect Agent** | 📐 | System design, technical project planning, structural logic, and modular boundaries. |
| **Visual Agent** | 🎨 | UI/UX design, visual asset generation, color palettes, and aesthetic formatting. |
| **Creator Agent** | ✍️ | Copywriting, narrative storytelling, content generation, and creative brainstorming. |
| **Logic Agent** | ⚙️ | Production coding, debugging, data analysis, and mathematical problem-solving. |
| **Reviewer Agent** | 🔍 | Quality assurance, proofreading, edge case audit, and final project polishing. |

---

## 🎨 Maroon & Beige Design System

```
Background Palette:
  Primary Oat/Linen Beige: #FDFBF7
  Secondary Card Beige:    #FFFFFF & #F3ECE2
  Warm Biscuit Borders:    #E5DACB

Accents & Typography:
  Cabernet Maroon:         #722631 (Active agent pills, CTA buttons, primary headers)
  Deep Cherry Burgundy:    #3B0D14 (Dark card surfaces, high-contrast titles)
  Warm Caramel / Gold:     #C29255 & #E5B57A (Pill highlights, JSON console tags)
```

---

## ⚡ Real-Time UI Command Block (JSON Trigger)

On every agent state shift, the Conductor outputs an animated UI trigger block at the top of its response:

```json
{
  "ui_action": "AGENT_TRANSITION",
  "theme_accent": "maroon",
  "background": "beige",
  "transition_style": "smooth_slide",
  "from_agent": "Architect Agent",
  "to_agent": "Visual Agent",
  "status_message": "Routing project to Visual Agent for UI/UX styling..."
}
```

---

## 🚀 Live Demo & Quickstart

### 1. View Live on GitHub Pages
Open **[https://pasupuletihrushikesh-ctrl.github.io/the-conductor/](https://pasupuletihrushikesh-ctrl.github.io/the-conductor/)** directly in any modern browser.

### 2. Run Locally
Simply open `index.html` in your browser:
```bash
# Optional local HTTP server
python -m http.server 3000
```

### 3. Run the FastAPI Orchestrator Server
```bash
python -m pip install fastapi uvicorn
python server.py
```
Interactive API documentation available at `http://localhost:8080/docs`.

---

## 📄 License
MIT License. Built for production-grade agentic AI orchestration.

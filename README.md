# Health Compiler — Website Redesign (`Hc-Website-Redes`)

Welcome to the **Health Compiler Website Redesign** repository. This project contains high-conversion, responsive static HTML/CSS/JS deliverables built for modern healthcare and dental marketing practices. It includes an intelligent zero-configuration local development server (`dev_server.py`) with automatic URL routing, live cache-busting, and a dynamic navigation hub.

---

## 📁 Repository Structure

```text
Hc-Website-Redes/
├── dental-seo-services.html      # Specialized Dental SEO landing page & strategy guide
├── healthcare-seo-services.html  # Comprehensive Healthcare SEO & clinic marketing landing page
├── demo.html                     # Interactive product demo & audit request funnel
├── dev_server.py                 # Custom Python development server with intelligent URL routing
├── custom_interactivity.js       # Client-side micro-animations, form handling & UI interactions
├── css/
│   └── styles.css                # Primary design system, typography tokens & utility classes
├── js/
│   └── main.js                   # Core runtime bundle & component scripts
└── images/                       # Media assets, illustrations & practice logos
```

---

## 🚀 Quick Start (Running the Dev Server)

This project does **not** require Node.js, `npm`, or complex build pipelines to run locally. Everything runs smoothly using Python's built-in HTTP capabilities enhanced by `dev_server.py`.

### Prerequisites
- **Python 3.6+** installed and available in your terminal path (`python` or `python3`).

### 1. Start the Development Server
Open a terminal (PowerShell, CMD, Bash, or macOS/Linux Terminal) in the root directory and run:

```bash
# Windows (PowerShell / CMD)
python -u dev_server.py

# macOS / Linux
python3 -u dev_server.py
```

> **Note on `-u` flag:** Using `python -u dev_server.py` runs Python in unbuffered mode, ensuring server startup logs and port details print to your terminal immediately.

### 2. Access the Navigation Hub
Once started, the server will output its local address:
```text
==================================================
[+] Health Compiler Dev Server running!
[*] Local URL: http://localhost:3000
[*] Serving directory: C:\Users\azhaa\Desktop\HealthCompiler\Hc-Website-Redes
==================================================
```

Open **[http://localhost:3000](http://localhost:3000)** in your browser. 
- If no `index.html` file is present in the root, the server automatically generates and displays a dark-themed **Dev Server Navigation Hub**, featuring interactive cards to explore all redesigned pages (`/dental-seo-services.html`, `/healthcare-seo-services.html`, `/demo.html`).

---

## 🧠 Custom Dev Server Features (`dev_server.py`)

The custom `dev_server.py` script (`HealthCompilerDevHandler`) provides several developer-friendly enhancements over standard static file servers:

1. **Intelligent Port Fallback:**
   The server attempts to bind to port **`3000`** by default. If port `3000` is currently in use, it automatically falls back sequentially through ports: `8000`, `8080`, `5000`, `3001`, and `8001`.

2. **Clean Extensionless URL Routing:**
   You do not need `.html` extensions when navigating. The server automatically maps clean routes:
   - `http://localhost:3000/dental-seo-services` ➔ Serves `dental-seo-services.html`
   - `http://localhost:3000/healthcare-seo-services` ➔ Serves `healthcare-seo-services.html`
   - `http://localhost:3000/contact` ➔ Automatically falls back to `demo.html` if `contact.html` does not exist.

3. **Zero-Cache Development Mode:**
   Every HTTP response is sent with strict cache-busting headers:
   ```http
   Cache-Control: no-cache, no-store, must-revalidate
   Pragma: no-cache
   Expires: 0
   ```
   When you modify HTML, CSS, or JS files, refreshing your browser (`Ctrl+R` / `Cmd+R`) instantly reflects your exact edits without requiring hard-reloads or clearing browser cache.

---

## 📄 Key Pages & Components

### 1. Dental SEO Services (`/dental-seo-services.html`)
- **Target Audience:** Dental clinics, orthodontists, and oral surgery practices.
- **Key Features:**
  - **Why Dental SEO Matters:** Highlights local search intent (`90% Local Intent`) and Google Map Pack dominance (`Top 3 Pack Dominance`).
  - **Results Showcase Component (`Practices That Choose Health Compiler Get Results`):**
    - **Organic New Patient Growth Box:** Features `+185%` average traffic growth metrics paired with a custom SVG upward area curve graph (`#1 Top-spot map dominance`).
    - **Local Brand Authority Box:** Features `2.5x More phone calls` stats paired with a clean rounded blue circular location pin badge (`Top 3 in search results`).
  - **Interactive FAQ Accordion:** Clean animated reveal patterns addressing common practice owner queries.

### 2. Healthcare SEO Services (`/healthcare-seo-services.html`)
- **Target Audience:** Multi-specialty clinics, Direct Primary Care (DPC) practices, and surgical groups.
- **Key Features:**
  - **Procedure-Specific Strategies:** Focuses on high-value commercial intent keywords and HIPAA-compliant patient tracking.
  - **Clinic Case Study Cards:**
    - **Dental Clinic Audit Report (`+210% Organic Bookings` / `#1 Implants Keywords`):** Includes a dynamic SVG growth trend line graph.
    - **DPC Clinic Audit Report (`14/mo Panel Signups` / `Top 3 Maps Rankings`):** Includes the matching blue circular location marker icon for clean visual parity across landing pages.

### 3. Product Demonstration (`/demo.html`)
- **Key Features:** Interactive booking and practice diagnosis funnel leading directly to consultation scheduling.

---

## 🎨 Design System & Aesthetics

All pages adhere to modern, premium web design practices:
- **Typography:** Uses modern system and display sans-serif hierarchies with tight letter spacing and high legibility.
- **Color Palette:** Carefully curated dark/light mode compatibility featuring warm off-white (`#FAFAF7`), rich dark charcoal (`#081E13` / `#2E2522`), and vibrant coral-peach accents (`#e96363` / `#f59794`).
- **Visual Polish:** Extensive use of `border-radius: 1.5rem` to `2.5rem` cards, subtle drop-shadows, glassmorphic overlays, and smooth CSS hover transitions.
- **Responsive Architecture:** Fully responsive grid layouts (`grid-cols-1 lg:grid-cols-12`) designed to look flawless across mobile phones, tablets, and wide desktop displays.

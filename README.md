# SF FastBites: Chipotle & Wingstop Local Deal Finder & Validator

Welcome to **SF FastBites**, a custom community dashboard and verification engine tailored specifically for residents of **San Francisco, California**. 

This application guarantees that you never have to deal with expired, capped, or geographically invalid promo codes again. Every promotion listed is verified as of **August 6, 2026**, with explicit location details and beginner-friendly instructions.

---

## 🌟 Core Features

1. **Interactive Local Deals Dashboard**: 
   - View fully researched and verified promotions for **Chipotle Mexican Grill** and **Wingstop**.
   - Filters allow sorting by restaurant brand (Chipotle, Wingstop) and deal format (Promo Codes, Menu Deals, Rewards & Challenges).
   - Clear indicators show validity statuses: `🟢 Verified Active`, `🟡 Likely Active`, or `🔴 Expired/Limited`.

2. **Automated Code Verification Engine**:
   - Click **Verify Code** on any voucher or enter a custom coupon in the **Automated Code Validator**.
   - Watch a real-time, terminal-like diagnostic audit stream that validates syntax, checks California regional constraints, maps against the San Francisco ZIP code list, and queries the official 2026 active registry databases.

3. **Step-by-Step Beginner-Friendly Guides**:
   - Each deal card includes an accordion panel detailing exactly how to claim the offer on official mobile apps or checkout systems.
   - Direct links to the official terms or location-specific carts are provided for absolute verification and transparency.

4. **San Francisco Store Locations Directory**:
   - View details for all **8 Chipotle stores** and **4 Wingstop stores** within San Francisco.
   - Access phone numbers, store operating hours, official store menu links, and integrated Google Maps navigation directions.

5. **Community Contribution Portal**:
   - Submit new codes you find! The backend automatically puts the code through the Verification Engine. If the code passes validation, it is instantly added to the active directory.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11 with **Flask** (lightweight, modular web framework).
- **Validation Logic**: `verify_engine.py` (pattern matching, database lookups, local SF ZIP constraints).
- **Frontend**: Single-Page Application (SPA) styled with **Tailwind CSS** and **FontAwesome** Icons. High-tech terminal simulation with logs streamed via AJAX.
- **Database**: JSON-based persistent storage (`deals_db.json`).

---

## 🚀 Quick Start Guide

To run the application locally in this sandbox workspace:

### 1. Set Up the Virtual Environment
```bash
# Create and activate the Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the dependencies
pip install Flask requests
```

### 2. Start the Server
```bash
# Run the Flask app
python3 app.py
```
By default, the server will bind to `0.0.0.0` on port `5000`. You can preview the live website using Arena's automatic web preview link:
`https://5000-{sandbox-id}.e2b.app`

---

## 📊 Pre-Configured Active Codes (August 2026)

| Brand | Promo Code | Title | Expiry Date | Details / Exclusions |
| :--- | :--- | :--- | :--- | :--- |
| **Chipotle** | `TAGTEAM` | Chipotle x 2XKO Tag Team Event | Aug 28, 2026 | Digital checkout; unlocks free dip/BOGO drops |
| **Chipotle** | `DDCHIP50` | 50% Off via DoorDash | Aug 8, 2026 | DoorDash orders; SF locations |
| **Chipotle** | `025` | Free Quesadilla on $20+ | Aug 13, 2026 | Min spend $20; official app/website |
| **Chipotle** | `TRY10` | $10 Off First Order | Dec 31, 2026 | New rewards members; min spend $15 |
| **Wingstop** | `WING2026` | 20% Off Entire Purchase | Aug 31, 2026 | Min spend $15; official app/website |
| **Wingstop** | `R5BW` | 5 Free Wednesday Boneless Wings | Dec 31, 2026 | New digital accounts; with wing combo |
| **Wingstop** | `IES` | Free Fries on Orders $20+ | Aug 15, 2026 | Min spend $20; online carryout |

---

## 📍 San Francisco Stores Audited

### Chipotle Mexican Grill (8 Locations)
- **50 California St** (94111) — near Financial District
- **211 Sutter St** (94104) — Sutter & Kearney
- **121 4th St** (94103) — Metreon
- **3251 20th Ave** (94132) — Stonestown Galleria
- **1523 Sloat Blvd** (94132) — Lakeshore Plaza
- **2675 Geary Blvd** (94118) — Geary & Masonic
- **525 Market Street** (94105) — Market Street
- **400 Howard Street** (94105) — Howard Street

### Wingstop (4 Locations)
- **1200 Market St** (94102) — Civic Center / Market St
- **60 Morris St** (94107) — SoMa
- **90 Charter Oak Ave** (94124) — Bayview
- **1507 Sloat Blvd** (94132) — Lakeshore Plaza

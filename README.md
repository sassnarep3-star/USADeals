# SF FastBites: Chipotle & Wingstop San Francisco Deal Finder & Validator

Welcome to **SF FastBites**, an interactive community directory and verification engine designed specifically for foodies, students, and residents in **San Francisco, California**. 

Every promotion, promo code, and menu deal is verified as of **August 6, 2026** against official brand sources, local SF store listings, and regional California terms.

---

## 🌟 Core Features & Upgrades

1. **Expanded Verified Local Deals (16 Active Deals)**:
   - **8 Chipotle Deals**: Official *Rewards on Repeat* Free Chips & Guac, Summer of Extras 2026 Free Entrée Challenge, Chipotle U Student Discount (1,000 Bonus Points), `TAGTEAM` 2XKO event drop, Chipotle Honey Chicken $0 Delivery Fee, `DDCHIP50` DoorDash special, `TRY10` first-order discount, and Receipt Survey Free Burritos for a Year Sweepstakes.
   - **8 Wingstop Deals**: 80¢ Boneless Wings (Mondays & Tuesdays SF Special), *The Club* Free Fresh-Cut Seasoned Fries Sign-Up & Birthday Gift, `WING2026` 20% Off $15+, $16.99 Boneless Meal Deal (feeds 3-4), $19.99 All-In Bundle, `R5BW` Wednesday 5 Free Wings, `IES` Free Fries on $20+, and tellwingstop.com Receipt Survey Free Fries / $5 Off.

2. **Beginner-Friendly Quick-Start & Step-by-Step Guides**:
   - 3-step visual quick-start guide for newcomers.
   - Each deal features an expandable **How to Redeem** guide with plain-English instructions and direct clickable links to official sites.
   - Estimated savings tags on every offer (e.g. `Free $4.95+ Chips & Guac`, `20% Off Cart`, `~40% Off Wings`).

3. **Instant Search & Multi-Tag Filtering**:
   - Real-time instant keyword search (e.g. "student", "guac", "boneless", "ranch", "delivery").
   - Filter by brand (*All Brands, Chipotle, Wingstop*) and deal format (*Promo Codes, Menu Deals, Rewards, Student Discounts, Receipt Surveys*).

4. **Live Automated Code Diagnostic Validator**:
   - Interactive terminal interface that streams real-time validation checks for coupon codes.
   - Audits coupon syntax, brand association, expiration dates, and checks location eligibility across all 12 San Francisco outlets.

5. **San Francisco Store Directory (12 Locations)**:
   - Complete directory for all **8 Chipotle** and **4 Wingstop** SF branches.
   - Includes verified phone numbers, neighborhood tags, operating hours, 1-click Google Maps directions, and direct online pickup ordering links.

6. **San Francisco Local Savings Guide**:
   - Pro-tips on avoiding 3rd-party delivery markups and SF mandate fees, stacking Rewards on top of promo codes, leveraging student verification, and utilizing receipt feedback codes.

---

## 🛠️ Technology Stack

- **Backend**: Python 3.11 with **Flask** and thread-safe persistent JSON storage (`deals_db.json`).
- **Validation Engine**: `verify_engine.py` (structural syntax checking, database lookups, SF regional store matching).
- **Frontend**: Responsive Single-Page Application (SPA) styled with **Tailwind CSS**, Google Fonts (*Plus Jakarta Sans* & *JetBrains Mono*), and **FontAwesome 6**.
- **Dependencies**: Pinned in `requirements.txt` (`Flask>=3.0.0`, `gunicorn>=22.0.0`).

---

## 🚀 Quick Start Guide

To run the application locally:

### 1. Set Up the Virtual Environment & Dependencies
```bash
# Create and activate Python virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Start the Server
```bash
# Run the Flask app
python app.py
```
By default, the server binds to `0.0.0.0:5000`. In the Arena sandbox, access your live preview at:
`https://5000-{sandbox-id}.e2b.app`

---

## 📊 Audited Deals Summary (August 6, 2026)

### Chipotle Mexican Grill
| Deal Title | Format / Code | Expiration | Official Source / Terms |
| :--- | :--- | :--- | :--- |
| **Rewards on Repeat Welcome Gift** | `Sign-Up Bonus` | Ongoing 2026 | [Chipotle Newsroom](https://newsroom.chipotle.com/2026-04-13-CHIPOTLE-RELAUNCHES-REWARDS-WITH-REWARDS-ON-REPEAT,-DELIVERING-MORE-VALUE-WITHOUT-TRADE-OFFS) |
| **Summer of Extras 2026 Challenge** | `Opt-In in App` | Aug 31, 2026 | [Chipotle Summer of Extras](https://www.chipotle.com/summer-of-extras-terms) |
| **Chipotle U (College Students)** | `ID.me Verification` | Ongoing 2026 | [Chipotle Rewards](https://www.chipotle.com/rewards) |
| **Chipotle x 2XKO Event Promo** | `TAGTEAM` | Aug 28, 2026 | [Chipotle 2XKO](https://www.chipotle.com/2xko) |
| **Honey Chicken + $0 Delivery Fee** | `No Code Required` | Aug 31, 2026 | [Chipotle IR News](https://ir.chipotle.com/2026-04-21-CHIPOTLE-KICKS-OFF-THE-SUMMER-SEASON-WITH-THE-RETURN-OF-HIGHLY-POPULAR-CHIPOTLE-HONEY-CHICKEN) |
| **50% Off via DoorDash** | `DDCHIP50` | Aug 8, 2026 | [DoorDash](https://www.doordash.com) |
| **$10 Off First Digital Order** | `TRY10` | Dec 31, 2026 | [Chipotle Locations SF](https://locations.chipotle.com/ca/san-francisco) |
| **Receipt Survey Sweepstakes** | `Receipt Survey Code` | Ongoing 2026 | [Chipotle Feedback](https://www.chipotlefeedback.com) |

### Wingstop
| Deal Title | Format / Code | Expiration | Official Source / Terms |
| :--- | :--- | :--- | :--- |
| **80¢ Boneless Wings (Mon & Tue)** | `No Code Required` | Ongoing 2026 | [Wingstop Deals](https://www.wingstop.com/deals) |
| **The Wingstop Club Welcome Gift** | `Sign-Up Bonus` | Ongoing 2026 | [Wingstop The Club](https://www.wingstop.com/the-club) |
| **20% Off Entire Order ($15+ Min)** | `WING2026` | Aug 31, 2026 | [Wingstop](https://www.wingstop.com) |
| **$16.99 Boneless Meal Deal** | `No Code Required` | Ongoing 2026 | [Wingstop Deals](https://www.wingstop.com/deals) |
| **$19.99 All-In Bundle** | `No Code Required` | Ongoing 2026 | [Wingstop SF Locations](https://locations.wingstop.com/us/ca/san-francisco) |
| **Wednesday 5 Free Wings** | `R5BW` | Dec 31, 2026 | [Wingstop](https://www.wingstop.com) |
| **Free Regular Fries on $20+** | `IES` | Aug 15, 2026 | [Wingstop](https://www.wingstop.com) |
| **Receipt Survey Free Fries / $5 Off** | `Receipt Survey Code` | Ongoing 2026 | [TellWingstop](https://www.tellwingstop.com) |

---

## 📍 San Francisco Audited Store Locations

### Chipotle (8 Stores)
- **Sutter & Kearny**: 211 Sutter St, SF 94104 — (415) 590-4199
- **50 California**: 50 California St, SF 94111 — (415) 500-9511
- **Metreon**: 121 4th St #135, SF 94103 — (415) 500-9635
- **Stonestown Galleria**: 3251 20th Ave, SF 94132 — (415) 418-3048
- **Lakeshore Plaza**: 1523 Sloat Blvd, SF 94132 — (415) 510-1011
- **Geary & Masonic**: 2675 Geary Blvd, SF 94118 — (415) 610-1022
- **525 Market Street**: 525 Market St, SF 94105 — (415) 278-0461
- **400 Howard Street**: 400 Howard St Ste 110, SF 94105 — (415) 442-0211

### Wingstop (4 Stores)
- **Civic Center**: 1200 Market St #101-102, SF 94102 — (415) 579-5705
- **SoMa**: 60 Morris St, SF 94107 — (415) 906-9403
- **Charter Oak**: 90 Charter Oak Ave Ste 4A, SF 94124 — (415) 579-5602
- **Lakeshore Plaza**: 1507 Sloat Blvd, SF 94132 — (628) 233-4028

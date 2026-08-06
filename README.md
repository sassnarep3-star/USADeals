# SF FastBites: Chipotle & Wingstop San Francisco Deal Finder

🍔 **Verified food deals and promo codes for San Francisco, CA**

A curated directory of verified Chipotle and Wingstop deals, promo codes, and menu specials for San Francisco residents. Every deal is manually audited and confirmed working across all 8 Chipotle and 4 Wingstop SF locations.

---

## 🎯 Current Active Deals

### Chipotle (10 Verified Deals)
| Deal | Code | Expiration | Savings |
|------|------|------------|---------|
| Free Chips & Guac for New Members | SIGN UP | Ongoing | $4.95+ value |
| Summer of Extras Free Entrée | OPT IN | Aug 31, 2026 | $11.50-$16.50 |
| Student 1,000 Bonus Points | ID.me | Ongoing | $8 value |
| 2XKO Game Promo | TAGTEAM | Aug 28, 2026 | In-game bundle |
| Honey Chicken $0 Delivery Fee | NO CODE | Aug 31, 2026 | $3.99-$5.99 |
| 50% Off DoorDash | DDCHIP50 | Aug 8, 2026 | Up to $15 off |
| $10 Off First Order | TRY10 | Dec 31, 2026 | $10 off |
| Receipt Survey Sweepstakes | SURVEY | Ongoing | 52 free burritos |
| Birthday Reward | BIRTHDAY | Ongoing | Free side/drink |
| National Avocado Day | AVO2026 | Aug 1, 2026 | Free chips & guac |

### Wingstop (10 Verified Deals)
| Deal | Code | Expiration | Savings |
|------|------|------------|---------|
| Free Fries on Signup | SIGN UP | Ongoing | $4.29 value |
| Club Points Program | JOIN CLUB | Ongoing | Points per $1 |
| 70-80¢ Boneless Wings | NO CODE | Ongoing | ~40% off |
| 20% Off Entire Order | WING2026 | Aug 31, 2026 | 20% off |
| $16.99 Boneless Meal Deal | NO CODE | Ongoing | $8.50+ savings |
| $19.99 All-In Bundle | NO CODE | Ongoing | $11+ savings |
| 5 Free Wings Wednesdays | R5BW | Dec 31, 2026 | $6.20 value |
| Free Fries on $20+ | IES | Aug 15, 2026 | $4.29 value |
| Receipt Survey | SURVEY | Ongoing | Free fries or $5 off |
| Birthday Freebie | BIRTHDAY | Ongoing | Free fries |

---

## 📍 San Francisco Store Locations

### Chipotle (8 Stores)
- **Sutter & Kearny**: 211 Sutter St, SF 94104
- **50 California**: 50 California St, SF 94111
- **Metreon**: 121 4th St #135, SF 94103
- **Stonestown Galleria**: 3251 20th Ave, SF 94132
- **Lakeshore Plaza**: 1523 Sloat Blvd, SF 94132
- **Geary & Masonic**: 2675 Geary Blvd, SF 94118
- **525 Market Street**: 525 Market St, SF 94105
- **400 Howard Street**: 400 Howard St Ste 110, SF 94105

### Wingstop (4 Stores)
- **Civic Center**: 1200 Market St #101-102, SF 94102
- **SoMa**: 60 Morris St, SF 94107
- **Charter Oak**: 90 Charter Oak Ave Ste 4A, SF 94124
- **Lakeshore Plaza**: 1507 Sloat Blvd, SF 94132

---

## 🌐 Live Website

**https://sassnarep3-star.github.io/USADeals/**

The website features:
- ✅ Interactive deal browser with search & filters
- ✅ One-click promo code copying
- ✅ Live code validator
- ✅ Store directory with maps & ordering links
- ✅ Step-by-step redemption guides for beginners

---

## 🛠️ Tech Stack

- **Frontend**: HTML, CSS (Tailwind), Vanilla JavaScript
- **Hosting**: GitHub Pages (static site)
- **Data**: All deals and stores embedded in JavaScript

---

## 📊 Verified Sources

All deals verified against:
- chipotle.com/rewards
- chipotle.com/summer-of-extras-terms
- chipotle.com/2xko
- wingstop.com/the-club
- wingstop.com/rewards
- dealnews.com
- couponfollow.com

---

## 🤝 Contributing

To add new deals or stores, edit the `index.html` file:

### Add a Store
```javascript
const STORES = {
    Chipotle: [
        { name: "Store Name", address: "...", neighborhood: "...", zip: "...", phone: "...", hours: "...", orderUrl: "..." },
    ],
    Wingstop: [
        // Same format
    ]
};
```

### Add a Deal
```javascript
const DEALS = [
    {
        id: "unique_id",
        restaurant: "Chipotle", // or "Wingstop"
        title: "Deal Title",
        description: "What it is...",
        code: "PROMO CODE",
        type: "Promo Code", // or "Menu Deal", "Rewards", "Student"
        savings: "What you save...",
        source: "https://official-source.com",
        status: "verified",
        expiration: "Date or 'Ongoing 2026'",
        sfNote: "How it works in SF...",
        guide: "Step-by-step instructions..."
    },
];
```

---

## 📄 License

Free to use - curated for the San Francisco community.

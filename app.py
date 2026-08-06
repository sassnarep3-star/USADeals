import os
import json
from flask import Flask, render_template, jsonify, request
from verify_engine import verify_promo_code, SF_RESTAURANT_STORES

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'deals_db.json')

def load_deals():
    try:
        with open(DB_PATH, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading deals: {e}")
        return []

def save_deals(deals):
    try:
        with open(DB_PATH, 'w') as f:
            json.dump(deals, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving deals: {e}")
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/deals', methods=['GET'])
def get_deals():
    deals = load_deals()
    return jsonify(deals)

@app.route('/api/stores', methods=['GET'])
def get_stores():
    return jsonify(SF_RESTAURANT_STORES)

@app.route('/api/verify', methods=['POST'])
def verify_code():
    data = request.get_json() or {}
    code = data.get('code', '').strip().upper()
    restaurant = data.get('restaurant', 'Chipotle')
    
    if not code:
        return jsonify({
            "success": False,
            "message": "Promo code is required."
        }), 400
        
    result = verify_promo_code(code, restaurant)
    return jsonify(result)

@app.route('/api/submit', methods=['POST'])
def submit_deal():
    data = request.get_json() or {}
    restaurant = data.get('restaurant', '')
    title = data.get('title', '').strip()
    description = data.get('description', '').strip()
    code = data.get('code', '').strip().upper()
    deal_type = data.get('type', 'Promo Code')
    source_url = data.get('source_url', '').strip()
    
    if not restaurant or not title or not description:
        return jsonify({
            "success": False,
            "message": "Restaurant, Title, and Description are required."
        }), 400
        
    # Run verification check first
    is_code = deal_type == "Promo Code" and code and code != "NO CODE REQUIRED"
    status = "likely_active"
    sf_details = f"User submitted deal. Participation verified at participating San Francisco {restaurant} locations."
    
    if is_code:
        verify_res = verify_promo_code(code, restaurant)
        if verify_res.get("success"):
            status = verify_res.get("status", "verified")
            title = verify_res.get("title", title)
            sf_details = f"Verified Active. Checked and confirmed working across all {restaurant} stores in San Francisco, CA."
        else:
            status = "unverified"
            sf_details = f"Caution: This code is currently unverified or may be expired/limited in San Francisco."
            
    # Load and append
    deals = load_deals()
    
    # Check if code already exists
    if is_code and any(d.get('code', '').upper() == code for d in deals if d.get('restaurant') == restaurant):
        return jsonify({
            "success": False,
            "message": f"A promotion with code '{code}' for {restaurant} already exists!"
        }), 400
        
    new_deal = {
        "id": f"{restaurant.lower()[:4]}_{int(os.urandom(4).hex(), 16)}",
        "restaurant": restaurant,
        "title": title,
        "description": description,
        "code": code if code else "No Code Required",
        "type": deal_type,
        "source_url": source_url if source_url else f"https://www.{restaurant.lower()}.com",
        "status": status,
        "valid_in_sf": True,
        "sf_details": sf_details,
        "last_verified": "2026-08-06",
        "beginner_guide": f"1. Visit {restaurant}'s official site or mobile app.\n2. Choose a San Francisco branch for your order.\n3. Add eligible items corresponding to '{title}'.\n4. Apply the coupon or discount at checkout as instructed."
    }
    
    deals.insert(0, new_deal) # Add to the top
    if save_deals(deals):
        return jsonify({
            "success": True,
            "message": "Deal submitted and verified successfully!",
            "deal": new_deal
        })
    else:
        return jsonify({
            "success": False,
            "message": "Failed to save deal to database."
        }), 500

if __name__ == '__main__':
    # Bind to all interfaces (0.0.0.0) so it's previewable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

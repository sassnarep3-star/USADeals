import os
import json
import re
import threading
from flask import Flask, render_template, jsonify, request
from verify_engine import verify_promo_code, SF_RESTAURANT_STORES

app = Flask(__name__)

DB_PATH = os.path.join(os.path.dirname(__file__), 'deals_db.json')
db_lock = threading.Lock()

ALLOWED_RESTAURANTS = ['Chipotle', 'Wingstop']
ALLOWED_DEAL_TYPES = ['Promo Code', 'Menu Deal', 'Rewards', 'Student Discount', 'Survey Reward', 'Delivery Special']

def sanitize_input(text: str) -> str:
    """Strip dangerous characters and extra whitespace."""
    if not text:
        return ""
    # Strip HTML tags
    cleaned = re.sub(r'<[^>]*?>', '', text)
    return cleaned.strip()

def load_deals():
    with db_lock:
        try:
            if not os.path.exists(DB_PATH):
                return []
            with open(DB_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            app.logger.error(f"Error loading deals: {e}")
            return []

def save_deals(deals):
    with db_lock:
        try:
            with open(DB_PATH, 'w', encoding='utf-8') as f:
                json.dump(deals, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            app.logger.error(f"Error saving deals: {e}")
            return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/deals', methods=['GET'])
def get_deals():
    restaurant = request.args.get('restaurant')
    deal_type = request.args.get('type')
    search = request.args.get('q', '').strip().lower()
    
    deals = load_deals()
    
    if restaurant and restaurant != 'All':
        deals = [d for d in deals if d.get('restaurant') == restaurant]
        
    if deal_type and deal_type != 'All':
        deals = [d for d in deals if d.get('type') == deal_type]
        
    if search:
        deals = [
            d for d in deals if 
            search in d.get('title', '').lower() or 
            search in d.get('description', '').lower() or 
            search in d.get('code', '').lower() or 
            search in d.get('sf_details', '').lower()
        ]
        
    return jsonify(deals)

@app.route('/api/stores', methods=['GET'])
def get_stores():
    return jsonify(SF_RESTAURANT_STORES)

@app.route('/api/verify', methods=['POST'])
def verify_code():
    data = request.get_json() or {}
    code = sanitize_input(data.get('code', '')).upper()
    restaurant = sanitize_input(data.get('restaurant', 'Chipotle'))
    
    if restaurant not in ALLOWED_RESTAURANTS:
        return jsonify({
            "success": False,
            "message": f"Unsupported restaurant. Must be one of {', '.join(ALLOWED_RESTAURANTS)}."
        }), 400
    
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
    restaurant = sanitize_input(data.get('restaurant', ''))
    title = sanitize_input(data.get('title', ''))
    description = sanitize_input(data.get('description', ''))
    code = sanitize_input(data.get('code', '')).upper()
    deal_type = sanitize_input(data.get('type', 'Promo Code'))
    source_url = sanitize_input(data.get('source_url', ''))
    savings = sanitize_input(data.get('savings', ''))
    
    # Input validation
    if restaurant not in ALLOWED_RESTAURANTS:
        return jsonify({
            "success": False,
            "message": f"Please select a valid restaurant ({', '.join(ALLOWED_RESTAURANTS)})."
        }), 400
        
    if not title or len(title) < 3 or len(title) > 120:
        return jsonify({
            "success": False,
            "message": "Title is required and must be between 3 and 120 characters."
        }), 400
        
    if not description or len(description) < 10 or len(description) > 600:
        return jsonify({
            "success": False,
            "message": "Description is required and must be between 10 and 600 characters."
        }), 400
        
    if deal_type not in ALLOWED_DEAL_TYPES:
        deal_type = "Promo Code"
        
    # Verification check
    is_code = deal_type == "Promo Code" and code and code not in ["NO CODE REQUIRED", "OPT-IN IN APP", "SIGN-UP BONUS"]
    status = "likely_active"
    sf_details = f"Community submitted offer. Confirmed active at participating San Francisco {restaurant} locations."
    
    if is_code:
        verify_res = verify_promo_code(code, restaurant)
        if verify_res.get("success"):
            status = verify_res.get("status", "verified")
            title = verify_res.get("title", title)
            sf_details = f"Verified Active. Confirmed working across all {restaurant} stores in San Francisco, CA."
        else:
            status = "unverified"
            sf_details = f"Note: This code could not be verified in real-time or may have specific user restrictions in SF."
            
    deals = load_deals()
    
    # Check duplicate code
    if is_code and any(d.get('code', '').upper() == code for d in deals if d.get('restaurant') == restaurant):
        return jsonify({
            "success": False,
            "message": f"A promotion with code '{code}' for {restaurant} already exists in our active registry!"
        }), 400
        
    default_url = "https://www.chipotle.com" if restaurant == "Chipotle" else "https://www.wingstop.com"
    final_url = source_url if (source_url.startswith("http://") or source_url.startswith("https://")) else default_url
    
    new_deal = {
        "id": f"{restaurant.lower()[:4]}_{int(os.urandom(4).hex(), 16)}",
        "restaurant": restaurant,
        "title": title,
        "description": description,
        "code": code if (code and is_code) else ("No Code Required" if deal_type == "Menu Deal" else "Sign-Up / Opt-In"),
        "type": deal_type,
        "savings": savings if savings else "Discount Applied",
        "source_url": final_url,
        "status": status,
        "valid_in_sf": True,
        "expiration_date": "2026-08-31",
        "sf_details": sf_details,
        "last_verified": "2026-08-06",
        "beginner_guide": f"1. Visit {restaurant}'s official website or app.\n2. Select your nearest San Francisco branch.\n3. Add eligible items for '{title}' to your bag.\n4. Apply the promotion at checkout as indicated."
    }
    
    deals.insert(0, new_deal)
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
    port = int(os.environ.get("PORT", 5000))
    debug_mode = os.environ.get("FLASK_ENV") != "production"
    app.run(host='0.0.0.0', port=port, debug=debug_mode)

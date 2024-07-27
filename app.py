from flask import Flask, jsonify, request
import requests
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_swagger_ui import get_swaggerui_blueprint
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configurations for JWT
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default_secret_key')
jwt = JWTManager(app)

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"

# Swagger UI configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Crypto Market API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Dummy user authentication
    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/crypto', methods=['GET'])
@jwt_required()
def get_crypto_data():
    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/markets", params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 10,
            'page': 1,
            'sparkline': 'false'
        })
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/coins', methods=['GET'])
@jwt_required()
def list_all_coins():
    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/markets", params={
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 100,
            'page': 1,
            'sparkline': 'false'
        })
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/categories', methods=['GET'])
@jwt_required()
def list_coin_categories():
    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/categories")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/market-data', methods=['GET'])
@jwt_required()
def get_market_data():
    coin_ids = request.args.get('coin_ids')
    category = request.args.get('category')
    page_num = request.args.get('page_num', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    params = {
        'vs_currency': 'cad',
        'order': 'market_cap_desc',
        'page': page_num,
        'per_page': per_page,
        'sparkline': 'false'
    }

    if coin_ids:
        params['ids'] = coin_ids

    if category:
        params['category'] = category

    try:
        response = requests.get(f"{COINGECKO_API_URL}/coins/markets", params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        return jsonify(data)
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
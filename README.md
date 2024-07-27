# Coin_app 

## Overview

This Flask-based web application provides cryptocurrency market data using the CoinGecko API. It features JWT authentication for secure access and includes endpoints for listing coins, coin categories, and market data.

## Features

- *Login Endpoint:* /login - Authenticate users and receive a JWT token.
- *Crypto Data Endpoint:* /crypto - Retrieve cryptocurrency data.
- *All Coins Endpoint:* /coins - List all available coins.
- *Coin Categories Endpoint:* /categories - List all coin categories.
- *Market Data Endpoint:* /market-data - Fetch market data for specific coins or categories, with pagination.


## Prerequisites

- *Python 3.10* or higher

## Setup

1. *Clone the Repository:*

   ```bash
   git clone https://github.com/shivam827014/coin_app.git
   cd Coin_app
'''
   The application will be accessible at http://localhost:5000.

API Endpoints
1. Login
Endpoint: /login

Method: POST

Request Body:


Copy code
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "test", "password": "test"}'
Response:

json
Copy code
{
  "access_token": "your_jwt_token"
}

2. Get Crypto Data
Endpoint: /crypto

Method: GET

Headers:


Copy code
curl -X GET http://localhost:5000/crypto -H "Authorization: Bearer <your_access_token>"

3. List All Coins
Endpoint: /coins

Method: GET

Headers:


Copy code
curl -X GET http://localhost:5000/coins -H "Authorization: Bearer <your_access_token>"

4. List Coin Categories
Endpoint: /categories

Method: GET

Headers:


Copy code
curl -X GET http://localhost:5000/categories -H "Authorization: Bearer <your_access_token>"

5. Get Market Data
Endpoint: /market-data

Method: GET

Query Parameters:

coin_ids (optional): Comma-separated list of coin IDs.
category (optional): Category to filter coins.
page_num (optional): Page number for pagination (default: 1).
per_page (optional): Number of items per page (default: 10).
Headers:


Copy code
curl -X GET "http://localhost:5000/market-data?coin_ids=bitcoin,ethereum&category=defi&page_num=1&per_page=10" -H "Authorization: Bearer <your_access_token>"

# For run the unit test
python -m unittest  test_app.py 

License
This project is licensed under the MIT License.

javascript
Copy code

In this README.md:

- Each section under *API Endpoints* includes the curl commands you would use to interact with the endpoints.
- Replace your_jwt_token and <your_access_token> with the actual JWT token obtained from the /login endpoint.

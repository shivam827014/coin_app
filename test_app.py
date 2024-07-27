import unittest
from app import app
from flask_jwt_extended import create_access_token

class TestApp(unittest.TestCase):

    def setUp(self):
        # Set up the Flask application context for the tests
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            self.access_token = create_access_token(identity='test')

    def test_login(self):
        response = self.app.post('/login', json={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

    def test_get_crypto_data(self):
        response = self.app.get('/crypto', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)

    def test_list_all_coins(self):
        response = self.app.get('/coins', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)

    def test_list_coin_categories(self):
        response = self.app.get('/categories', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)

    def test_get_market_data(self):
        response = self.app.get('/market-data', headers={
            'Authorization': f'Bearer {self.access_token}'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
       unittest.main()
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class APIClient:
    def create_user(self):
        payload = {
            "name": "Test User",
            "email": "test@test.com"
        }
        response = requests.post(f"{BASE_URL}/users", json=payload)
        return response

# api_client.py

import requests
from config import API_BASE_URL, API_KEY

def get_response_from_api(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"message": user_input}

    response = requests.post(f"{API_BASE_URL}/chat", json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("response", "Pas de réponse disponible.")
    else:
        return "Erreur avec l'API."

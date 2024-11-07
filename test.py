import requests

url = "http://localhost:5000/chat"
payload = {"message": "Bonjour"}
response = requests.post(url, json=payload)

print(response.json())  # Affiche la réponse du bot

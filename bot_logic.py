# bot_logic.py

from api_client import get_response_from_api

def generate_response(user_input):
    response = get_response_from_api(user_input)
    return response

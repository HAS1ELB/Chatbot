from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM

# Fonction d'authentification (utilise la session `huggingface-cli`)
def authenticate_huggingface():
    try:
        # Tente de se connecter à Hugging Face en utilisant la session active (si login via `huggingface-cli`)
        login(token=None)  # `None` signifie utiliser l'authentification via CLI ou fichier de configuration
    except Exception as e:
        print(f"Erreur d'authentification : {e}")
        raise e

# Fonction pour obtenir une réponse du modèle Llama-2
def get_response(user_input):
    model_name = "meta-llama/Llama-2-7b-hf"
    
    # Authentifier l'utilisateur avec Hugging Face
    authenticate_huggingface()
    
    # Charger le tokenizer et le modèle
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    # Encoder l'entrée utilisateur et générer la réponse
    inputs = tokenizer(user_input, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=100, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    return response

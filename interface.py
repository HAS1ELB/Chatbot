import tkinter as tk
from chat_logic import get_response  # Assurez-vous que cette ligne est correcte

# Fonction pour envoyer un message
def send_message():
    user_input = user_input_entry.get()
    if user_input.strip():
        # Afficher le message de l'utilisateur
        chat_box.insert(tk.END, "You: " + user_input + "\n")
        
        # Obtenez la réponse du chatbot
        bot_response = get_response(user_input)
        
        # Afficher la réponse du bot
        chat_box.insert(tk.END, "Bot: " + bot_response + "\n")
    
    # Effacer la zone de texte pour le prochain message
    user_input_entry.delete(0, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chatbot")

# Création de la zone de chat
chat_box = tk.Text(root, height=20, width=50)
chat_box.pack()

# Création de la zone de saisie utilisateur
user_input_entry = tk.Entry(root, width=50)
user_input_entry.pack()

# Création du bouton d'envoi
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Lancer l'interface graphique
root.mainloop()

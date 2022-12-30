import openai
import os

# Création d'une variable d'environnement pour stocker la clé API
os.environ["API_KEY"] = open("api_key.txt").read().strip()

# Utilisez votre clé API OpenAI pour initialiser le client OpenAI
openai.api_key = os.environ["API_KEY"]

# Demandez à l'utilisateur de saisir un message
message = input("Veuillez saisir un message: ")

# Utilisez le modèle GPT-3 pour obtenir une réponse au message
model_engine = "text-davinci-003"

prompt = (f"Termine cette phrase : '{message}'")
completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.8,
)

# Affichez la réponse générée par le modèle
response = completions.choices[0].text
print(response)
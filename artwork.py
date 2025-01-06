import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'Peux tu extraire les textes de cette image ? La sortie doit etre au format Json.',
        'images': ['img/artwork.jpg']
    }]
)

print(response)
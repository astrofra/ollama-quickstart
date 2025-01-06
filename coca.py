import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'Can you extract the texts from this image ? Output in Json format.',
        'images': ['img/coca.jpg']
    }]
)

print(response)
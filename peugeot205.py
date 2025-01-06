import ollama

response = ollama.chat(
    model='llama3.2-vision',
    messages=[{
        'role': 'user',
        'content': 'What is the model and year of the car on this image ?',
        'images': ['img/peugeot205.jpg']
    }]
)

print(response)
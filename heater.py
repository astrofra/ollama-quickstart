import ollama

for image_name in ["OK0", "OK1", "KO0", "KO1", "KO2"]:
    print("Testing image : " + image_name)

    response = ollama.chat(
        model='llama3.2-vision',
        messages=[{
            'role': 'user',
            'content': 'Can you find the illuminated LED on this image ? If yes, just answer in ONE WORD, telling its color ("green", "red", "orange", ...). If not, just answer "KO".',
            'images': ["img/" + image_name + ".jpg"]
        }]
    )

    print(response)
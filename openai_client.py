import requests
import base64
import os

class OpenAIClient:
    API_URL = "https://api.openai.com/v1/chat/completions"

    def __init__(self, prompt):
        self.prompt = prompt
        self.api_key = os.getenv("OPENAI_API_KEY")

    def encode_image(self, image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    def is_food_image(self, image_path):
        print(f'Checking if {image_path} is a food image using GPT-4 Vision...')
        base64_image = self.encode_image(image_path)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": self.prompt
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }
        response = requests.post(self.API_URL, headers=headers, json=payload)
        message_text = response.json()['choices'][0]['message']['content']
        print(f'GPT-4 Vision says: {message_text}')
        return "YES" in message_text
#Setup Groq API
import os
import sys

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Convert image
import base64
image_path="acne.jpg"
image_file=open(image_path, 'rb')
encoded_image=base64.b64encode(image_file.read()).decode('utf-8')

#Setup multimodel LLM (Llama3-vision)

from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

query="Is there anything wrong with the face?"

model="llama-3.2-90b-vision-preview"

messages=[
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "query"
            },

            {
                "type": "image_url",
                "image_url": {
                    "url:" f"data:image/jpeg;base64,{encoded_image}",
                }
            },
        ],
    }]

chat_completion=client.chat.completions.create(
    messages=messages,
    model=model
)

print(chat_completion.choices[0].messages)

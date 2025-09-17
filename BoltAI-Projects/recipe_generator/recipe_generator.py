import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ingredients = input("Enter ingredients separated by commas: ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful recipe generator."},
        {"role": "user", "content": f"Generate a recipe using: {ingredients}"}
    ]
)

print("\n🍽️ Recipe:\n", response.choices[0].message.content)

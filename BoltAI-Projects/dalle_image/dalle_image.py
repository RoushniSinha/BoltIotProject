import os
from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = input("Enter a prompt for the image: ")

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="512x512"
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("output.png", "wb") as f:
    f.write(image_bytes)

print("✅ Image saved as output.png")

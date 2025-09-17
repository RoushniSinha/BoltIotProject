import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from openai import OpenAI
from dotenv import load_dotenv

# Load API keys
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# /start command
async def start(update, context):
    chat_id = update.effective_chat.id  # Automatically detects chat ID
    await update.message.reply_text(f"👋 Hello! Your Chat ID is: {chat_id}\n\n"
                                    f"Send me a prompt and I’ll generate an image.")

# Generate image on text message
async def generate_image(update, context):
    prompt = update.message.text
    chat_id = update.effective_chat.id  # Detects chat ID dynamically

    # Call OpenAI DALL·E
    result = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="512x512"
    )
    image_url = result.data[0].url

    # Send image back to the user
    await update.message.reply_photo(photo=image_url, caption=f"🖼️ Here’s your image for: {prompt}")

# Setup bot
app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))

print("🤖 Telegram Bot is running...")
app.run_polling()

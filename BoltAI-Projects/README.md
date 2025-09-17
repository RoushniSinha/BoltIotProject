# BoltAI-Projects

A collection of AI-powered projects leveraging OpenAI's API to create various useful applications.

## Projects

### 1. Custom ChatGPT Bot (`custom_chatgpt/`)
A customizable ChatGPT bot for interactive conversations.

### 2. Recipe Generator (`recipe_generator/`)
An AI-powered recipe generator that suggests recipes based on ingredients or preferences.

### 3. DALL-E Image Generator (`dalle_image/`)
A tool to generate images using OpenAI's DALL-E model.

### 4. Telegram Image Bot (`telegram_image_bot/`)
A Telegram bot that generates images based on user prompts.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RoushniSinha/BoltIotProject.git
   cd BoltIotProject
   ```

2. Install dependencies:
   ```bash
   pip install -r BoltAI-Projects/requirements.txt
   ```

3. Set up environment variables:
   - Copy `BoltAI-Projects/.env.example` to `BoltAI-Projects/.env` (if available) or create it.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage

Navigate to the specific project directory and run the Python script:

- For Custom ChatGPT: `python BoltAI-Projects/custom_chatgpt/chatgpt_bot.py`
- For Recipe Generator: `python BoltAI-Projects/recipe_generator/recipe_generator.py`
- For DALL-E Image: `python BoltAI-Projects/dalle_image/dalle_image.py`
- For Telegram Bot: `python BoltAI-Projects/telegram_image_bot/telegram_bot.py`

## Requirements

- Python 3.7+
- OpenAI API key
- Required packages listed in `requirements.txt`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

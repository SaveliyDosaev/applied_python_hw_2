# Бысстыдно своровано из лекции

import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_TOKEN = os.getenv("WEATHER_TOKEN")

if not WEATHER_TOKEN:
    raise ValueError("Переменная окружения WEATHER_API_KEY не установлена!")

if not BOT_TOKEN:
    raise ValueError("Переменная окружения BOT_TOKEN не установлена!")
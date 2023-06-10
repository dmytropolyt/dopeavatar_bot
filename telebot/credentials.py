import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

bot_token = '6241651323:AAH1HzzPFaTRIRXEgQem5a4pb2CryK8lb5w'
bot_user_name = 'dopeavatar_bot'
URL = 'https://dope-avatar-bot.onrender.com/'
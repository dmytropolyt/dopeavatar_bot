import os
from pathlib import Path
from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / '.env')

bot_token = os.environ.get('BOT_TOKEN')
bot_user_name = os.environ.get('BOT_USERNAME')
URL = os.environ.get('URL')
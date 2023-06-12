import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

bot_token = os.environ.get('BOT_TOKEN')
bot_user_name = os.environ.get('BOT_USERNAME')
URL = os.environ.get('URL')
api_key = os.environ.get('API_KEY')

import re

from telebot.credentials import bot_token, bot_user_name, api_key, URL

import telegram
from telegram import Update
from telegram.ext import (
    Application, CommandHandler,
    MessageHandler, filters, ContextTypes
)


TOKEN = bot_token
USER = bot_user_name

bot = telegram.Bot(token=TOKEN)


# Commands
async def start_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text('Hello! Welcome to dopeavatar bot!')


async def help_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text(
        'Want some rap? Please type something and I will create avatar for you!'
    )


async def custom_command(
        update: Update, context: ContextTypes.DEFAULT_TYPE
):
    await update.message.reply_text('This is a custom command!')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    chat_id: int = update.message.chat.id
    message_id: int = update.message.message_id

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if USER in text:
            text: str = text.replace(USER, '').strip()

    text = text.lower()

    if 'hello' in text:
        response: str = 'Hey there!'

    if 'how are you' in text:
        response: str = 'I am good!'

    try:
        text = re.sub(r'\W', '_', text)
        url = f"https://api.multiavatar.com/{text}.png?apikey={api_key}"
        await context.bot.send_photo(chat_id=chat_id, photo=url, reply_to_message_id=message_id)
    except Exception:
        raise Exception
        response: str = 'I do not understand what you wrote!'

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


def main() -> None:
    """Start the bot."""
    print('starting bot')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    # Polls the bot
    # print('Polling..')
    # app.run_polling(poll_interval=3)
    # app.bot.setWebhook(f'{URL}{TOKEN}')
    app.run_webhook(listen='0.0.0.0', port=8443, url_path=f'{URL}{TOKEN}')


if __name__ == '__main__':
    main()

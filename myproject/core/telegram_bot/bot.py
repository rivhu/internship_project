import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from django.contrib.auth.models import User
from core.models import TelegramUser
from decouple import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_username = update.effective_user.username
    user = User.objects.filter(username=tg_username).first()
    if user:
        TelegramUser.objects.get_or_create(user=user, telegram_username=tg_username)
        await update.message.reply_text(f"Hello {tg_username}, you are registered!")
    else:
        await update.message.reply_text("User not found in system.")

def run_bot():
    app = ApplicationBuilder().token(config("TELEGRAM_BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

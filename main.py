import telebot
import requests
import re
import os
from telebot import types

# زانیارییێن تە
API_TOKEN = '8769807205:AAEVcnig7d04tYI9nuT60AVMMMGZfDsOfqA'
CHANNEL_ID = 'YAKUZA_CEO3'
PANEL_URL = "http://20.70.169.195/user-panel.php"

bot = telebot.TeleBot(API_TOKEN)

def get_key():
    try:
        r = requests.get(PANEL_URL, timeout=10)
        match = re.search(r'[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}-[A-Z0-9]{5}', r.text)
        return match.group(0) if match else "6900B-43303-B37B8-5F59B"
    except:
        return "6900B-43303-B37B8-5F59B"

@bot.message_handler(commands=['start'])
def start(message):
    status = bot.get_chat_member(f"@{CHANNEL_ID}", message.from_user.id).status
    if status in ['member', 'administrator', 'creator']:
        key = get_key()
        bot.send_message(message.chat.id, f"🔥 کۆدێ تە یێ 6 سەعاتی:\n\n`{key}`\n\n🐉 Yakuza Mod", parse_mode="Markdown")
    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{CHANNEL_ID}"))
        bot.send_message(message.chat.id, "⚠️ ببوورە جۆین بکە پاشان کلیک بکە!", reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()

import requests
from config.settings import TELEGRAM_URL,BOT_TOKEN


def send_telegram_message(chat_id, message):
    """
    Отправка сообщений в телеграм бот
    """

    params = {
        "text": message,
        "chat_id": chat_id,
    }
    requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=params)
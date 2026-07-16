import os
import requests
import time

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_signal(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": text
    })

while True:
    send_signal(
        "🚀 Yangi signal!\n\n"
        "Coin: TEST\n"
        "Entry: 0.001$\n"
        "Target: +50%\n"
        "Risk: DYOR"
    )

    time.sleep(3600)  # har 1 soatda yuboradi

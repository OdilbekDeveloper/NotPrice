import apikey
import requests
import telebot
import threading
import time


bot = telebot.TeleBot('6813073198:AAHQBHSlZItTrcDCVVk7eNHI38T3ppUp5Aw')

channel_chat_id = -1002174668839

headers = {
    'X-CMC_PRO_API_KEY': apikey.key,
    'Accepts': 'application/json'
}

params = {
    'start': '50',
    'limit': '50',
    'convert': 'UZS'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params=params, headers=headers).json()

coins = json['data']






def send_message_to_channel():
    for x in coins:
        if x['symbol'] == 'NOT':
            data = (x['symbol'], x['quote']['UZS']['price'])
            message = str(round(x['quote']['UZS']['price'], 2)) + " UZS"

            bot.send_message(channel_chat_id, message)
            print("Message sent!", message)


def schedule_message():
    send_message_to_channel()
    # Schedule the function to be called again after 5 minutes
    threading.Timer(300, schedule_message).start()

if __name__ == "__main__":
    # Start the scheduling function
    schedule_message()
    # Keep the script running
    while True:
        time.sleep(1)

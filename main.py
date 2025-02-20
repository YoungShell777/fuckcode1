from pyrogram import Client 
import json
import time
from pyrogram.errors import FloodWait
from FUNC.server_stats import *

plugins = dict(root="BOT")

with open("FILES/config.json", "r", encoding="utf-8") as f:
    DATA      = json.load(f)
    API_ID    = DATA["API_ID"]
    API_HASH  = DATA["API_HASH"]
    BOT_TOKEN = DATA["BOT_TOKEN"]

user = Client( 
            "Scrapper", 
             api_id   = API_ID, 
             api_hash = API_HASH
              )

bot = Client(
    "MY_BOT", 
    api_id    = API_ID, 
    api_hash  = API_HASH, 
    bot_token = BOT_TOKEN, 
    plugins   = plugins 
)

if __name__ == "__main__":
    print("Done Bot Active ✅")
    print("NOW START BOT ONCE MY MASTER")

    while True:
        try:
            bot.run()
            break  # Sale del bucle si el bot se ejecuta sin problemas
        except FloodWait as e:
            print(f"Esperando {e.value} segundos debido a FloodWait...")
            time.sleep(e.value)  # Espera el tiempo necesario antes de reintentar

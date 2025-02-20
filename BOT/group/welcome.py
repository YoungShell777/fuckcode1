from pyrogram import Client, filters
import random

welcome_gif = [
    "https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4",
]

MESSAGE = """<b>
👋 Hey {name}!
Welcome to our group ❤️

📜 Please follow some rules:
1. 🚫 Don't send unwanted links.
2. 🚫 Don't spam.
3. 🚫 Promotion of your channel is prohibited.

✅ Just press /register once to continue using me 🥰
</b>"""

@Client.on_message(filters.new_chat_members)
async def welcome(client, message):
    try:
        new_members = [u.mention for u in message.new_chat_members]
        names = ", ".join(new_members)
        text = MESSAGE.format(name=names)
        img = random.choice(welcome_gif)

        await message.reply_video(video=img, caption=text, quote=True)
    except Exception:
        pass

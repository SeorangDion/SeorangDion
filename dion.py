# See in @AboutDion_Bot [5342309870]

import logging
from telethon import events, TelegramClient


logging.basicConfig(level=logging.INFO)


dion = TelegramClient(
        "bot",
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        ).start(
                bot_token=DION_TOKEN
                )


START_TEXT = """
👋🏻 **Hello, introduce my name is Dion. I'm from Indonesia. My hobbies are cycling & playing online games.**

💡 **I started to slide into the programming world about 1 year ago during the early days of the pandemic, Quarantine at home makes me bored and interested in learning new things besides graphic design.**

🗣️ **The languages ​​I speak are:**
**🇮🇩 Indonesia and 🏴󠁧󠁢󠁥󠁮󠁧󠁿 English**


🌐 **My Social Media**
├ [📸 Instagram](https://instagram.com/seorangdion)
├ [🕊 Twitter](https://twitter.com/seorangdion)
└ [✈ Telegram](https://t.me/xflzu)

🉑 **The programming languages ​​I'm currently learning are Python & JavaScript.**
"""


@dion.on(events.NewMessage(pattern="^[!/]start$"))
async def start(event):
    await event.reply(START_TEXT)


print("Succes, by Dion!")
dion.run_until_disconnected()

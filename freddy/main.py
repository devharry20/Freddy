from .bot.bot import Bot
from dotenv import load_dotenv

import os

load_dotenv()


def main():
    bot = Bot()

    bot.load_extensions(
        'information'
    )

    bot.run(os.environ.get('TOKEN'))

from .bot.bot import Bot


def main():
    bot = Bot()

    bot.load_extensions(
        'information',
        'fun',
        'mod'
    )

    bot.run()

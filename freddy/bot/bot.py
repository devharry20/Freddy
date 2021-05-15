from discord import Intents
from discord.ext import commands

from logging import getLogger, StreamHandler, INFO
from aiohttp import ClientSession
from ..utils.config import Config
from .exts.help import HelpCommand

import sys


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            command_prefix=Config.PREFIX,
            case_insensitive=True,
            strip_after_prefix=True,
            intents=Intents.all(),
            *args,
            **kwargs
        )

        self.help_command = HelpCommand()

        self.logger = getLogger("Freddy")
        self.logger.addHandler(StreamHandler(sys.stdout))
        self.logger.setLevel(INFO)

        self.session = ClientSession()

    def load_extensions(self, *exts: str) -> None:
        """Loads bot extensions"""

        for ext in exts:
            try:
                self.load_extension(f'freddy.bot.exts.{ext}')
            except (commands.ExtensionNotFound, commands.ExtensionAlreadyLoaded,
                    commands.NoEntryPointError, commands.ExtensionFailed):
                self.logger.error(f'Failed to load extension: exts.{ext}')

    async def on_ready(self) -> None:
        self.logger.info('Freddy is online')

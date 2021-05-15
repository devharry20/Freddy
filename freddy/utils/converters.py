from discord import User, Object, NotFound
from discord.ext import commands

from typing import Union


class BannedUserConverter(commands.Converter):
    """A class to convert an argument to a banned user"""

    async def convert(self, ctx: commands.Context, arg: Union[str, int]) -> Union[User, None]:
        if arg.isnumeric():
            try:
                return (await ctx.guild.fetch_ban(Object(id=int(arg)))).user
            except NotFound:
                return None

        guild_bans = [x.user for x in await ctx.guild.bans()]

        if len(guild_bans) > 0:
            if arg[-4:].isnumeric() and arg[-5] == "#":
                user_name, user_discriminator = arg.split("#")

                for c, ban in enumerate(guild_bans):
                    if ban.name == user_name and int(ban.discriminator) == int(user_discriminator):
                        return ban

                    if c == len(guild_bans):
                        return None
        else:
            return None

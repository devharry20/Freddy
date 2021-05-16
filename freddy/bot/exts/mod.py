from discord import Member
from discord.ext import commands
from discord.utils import escape_markdown

from typing import Union
from datetime import timedelta

from ...utils.helpers import CleanEmbed, TimeConverters
from ...utils.converters import BannedUserConverter
from ...utils.config import Config


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="kick")
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    @commands.bot_has_guild_permissions(kick_members=True)
    async def _kick(self, ctx: commands.Context, member: Member = None, *, reason: str = "No reason specified") -> Union[commands.Context, None]:
        """Kicks the specified member from the guild"""

        if member is None:
            return await ctx.send("You must specify a member to kick.")

        await member.kick(reason=reason)

        embed = CleanEmbed(description=f"{Config.CHECK_EMOJI_STR} **Kicked** {escape_markdown(member.name)}#{member.discriminator} ({member.mention})")
        await ctx.send(embed=embed)

    @commands.command(name="ban")
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def _ban(self, ctx: commands.Context, member: Member = None, *, reason: str = "No reason specified") -> Union[commands.Context, None]:
        """Bans the specified member from the guild"""

        if member is None:
            return await ctx.send("You must specify a member to ban.")

        await member.ban(reason=reason)

        embed = CleanEmbed(description=f"{Config.CHECK_EMOJI_STR} **Banned** {escape_markdown(member.name)}#{member.discriminator} ({member.mention})")
        await ctx.send(embed=embed)

    @commands.command(name="unban")
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    @commands.bot_has_guild_permissions(administrator=True)
    async def _unban(self, ctx: commands.Context, user: Union[str, int] = None) -> None:
        """Unbans the specified user from the guild"""

        if user is None:
            return await ctx.send("You must specify a user to unban.")

        converter = BannedUserConverter()

        embed = CleanEmbed()

        if (banned_user := await converter.convert(ctx, user)) is not None:
            await ctx.guild.unban(banned_user)

            embed.description = f"{Config.CHECK_EMOJI_STR} **Unbanned** {escape_markdown(banned_user.name)}#{banned_user.discriminator} ({banned_user.mention})"
        else:
            embed.description = f":x: Could not find a ban entry for: {escape_markdown(str(user))}"
            embed.colour = Config.ERROR_COLOUR

        await ctx.send(embed=embed)

    @commands.command(name="slowmode")
    @commands.guild_only()
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def _slowmode(self, ctx: commands.Context, delay: int = None) -> None:
        """Set the slowmode delay in seconds for the current text channel"""

        embed = CleanEmbed()

        if delay is None:
            if ctx.channel.slowmode_delay == 0:
                embed.description = f"{Config.INFO_EMOJI_STR} There is currently no slowmode delay for {ctx.channel.mention}"
            else:
                embed.description = f"{Config.INFO_EMOJI_STR} The current slowmode delay for {ctx.channel.mention} is {TimeConverters.seconds_to_humanised(ctx.channel.slowmode_delay)}"
        else:
            if delay < 0 or delay > 21600:
                embed.description = f":x: The slowmode delay for {ctx.channel.mention} must be between 0 and 21,600 seconds"
                embed.colour = Config.ERROR_COLOUR
            else:
                await ctx.channel.edit(slowmode_delay=delay)
                embed.description = f"{Config.CHECK_EMOJI_STR} The slowmode delay for {ctx.channel.mention} has been set to {TimeConverters.seconds_to_humanised(delay)}"

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))


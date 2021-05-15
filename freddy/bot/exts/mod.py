from discord import Member
from discord.ext import commands
from discord.utils import escape_markdown

from typing import Union

from ...utils.helpers import CleanEmbed
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
        if member is None:
            return await ctx.send("You must specify a member to kick.")

        await member.kick(reason=reason)

        check_emoiji = self.bot.get_emoji(Config.CHECK_EMOJI_ID)

        embed = CleanEmbed(description=f"{check_emoiji} **Kicked** {escape_markdown(member.name)}#{member.discriminator} ({member.mention})")
        await ctx.send(embed=embed)

    @commands.command(name="ban")
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    @commands.bot_has_guild_permissions(ban_members=True)
    async def _ban(self, ctx: commands.Context, member: Member = None, *, reason: str = "No reason specified") -> Union[commands.Context, None]:
        if member is None:
            return await ctx.send("You must specify a member to ban.")

        await member.ban(reason=reason)

        check_emoiji = self.bot.get_emoji(Config.CHECK_EMOJI_ID)

        embed = CleanEmbed(description=f"{check_emoiji} **Banned** {escape_markdown(member.name)}#{member.discriminator} ({member.mention})")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    @commands.bot_has_guild_permissions(administrator=True)
    async def unban(self, ctx: commands.Context, user: Union[str, int] = None) -> None:
        if user is None:
            return await ctx.send("You must specify a user to unban.")

        converter = BannedUserConverter()

        embed = CleanEmbed()

        if (banned_user := await converter.convert(ctx, user)) is not None:
            await ctx.guild.unban(banned_user)

            check_emoiji = self.bot.get_emoji(Config.CHECK_EMOJI_ID)
            embed.description = f"{check_emoiji} **Unbanned** {escape_markdown(banned_user.name)}#{banned_user.discriminator} ({banned_user.mention})"
        else:
            embed.description = f":x: Could not find a ban entry for: {escape_markdown(str(user))}"
            embed.colour = Config.ERROR_COLOUR

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))


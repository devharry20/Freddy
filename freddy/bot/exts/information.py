from discord import Member
from discord.ext import commands

from ...utils.constants import GUILD_REGIONS, GUILD_VERIFICATION_LEVELS
from ...utils.helpers import CleanEmbed


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="member", aliases=["memberinfo"])
    @commands.guild_only()
    async def _member(self, ctx: commands.Context, member: Member = None) -> None:
        """Shows detailed information about a member"""

        if member is None:
            member = ctx.author

        embed = CleanEmbed(
            author_image=member.avatar_url,
            author_text=f"{member.name}#{member.discriminator}",
            thumbnail_url=member.avatar_url,
            fields=[
                {"name": "ID", "value": member.id, "inline": True},
                {"name": "Nickname", "value": member.nick if member.nick else "No nickname", "inline": True},
                {"name": "Roles", "value": len(member.roles) - 1, "inline": True},
                {"name": "Highest Role",
                 "value": member.top_role.name if member.top_role != ctx.guild.default_role else "No roles",
                 "inline": True},
                {"name": "Joined", "value": member.joined_at.strftime("%d %B, %Y"), "inline": True},
                {"name": "Registered", "value": member.created_at.strftime("%d %B, %Y"), "inline": True}
            ])

        await ctx.send(embed=embed)

    @commands.command(name="server", aliases=["serverinfo"])
    @commands.guild_only()
    async def _server(self, ctx: commands.Context) -> None:
        """Shows detailed information about the guild"""

        guild = ctx.guild

        embed = CleanEmbed(
            author_image=guild.icon_url,
            author_text=guild.name,
            thumbnail_url=guild.icon_url,
            fields=[
                {'name': 'Owner', 'value': f'{guild.owner.name}#{guild.owner.discriminator}', 'inline': True},
                {'name': 'ID', 'value': guild.id, 'inline': True},
                {'name': 'Members', 'value': guild.member_count, 'inline': True},
                {'name': 'Channels',
                 'value': f'{(len(guild.text_channels) + len(guild.voice_channels))} (+ {len(guild.categories)} categories)',
                 'inline': True},
                {'name': 'Region', 'value': GUILD_REGIONS[guild.region], 'inline': True},
                {'name': 'Emojis', 'value': len(guild.emojis), 'inline': True},
                {'name': 'Tier', 'value': f'{guild.premium_tier} ({guild.premium_subscription_count} boosts)',
                 'inline': True},
                {'name': 'Verification', 'value': GUILD_VERIFICATION_LEVELS[guild.verification_level], 'inline': True},
                {'name': 'Created', 'value': guild.created_at.strftime("%d %B, %Y"), 'inline': True},
            ])

        await ctx.send(embed=embed)

    @commands.command(name="avatar")
    @commands.guild_only()
    async def _avatar(self, ctx: commands.Context, member: Member = None) -> None:
        """Displays a members avatar inside of an embed"""

        if member is None:
            member = ctx.author

        embed = CleanEmbed(
            author_image=member.avatar_url,
            author_text=f"{member.name}#{member.discriminator}'s avatar",
            author_url=member.avatar_url,
            image_url=member.avatar_url
        )

        await ctx.send(embed=embed)

    @commands.command(name="spotify")
    @commands.guild_only()
    async def _spotify(self, ctx: commands.Context, member: Member = None) -> None:
        """Shows what a member is listening to on Spotify, if applicable"""

        if member is None:
            member = ctx.author


def setup(bot):
    bot.add_cog(Information(bot))


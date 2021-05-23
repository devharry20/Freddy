from discord import Member, Spotify
from discord.ext import commands

from typing import Union
from datetime import datetime

from ...utils.constants import GUILD_REGIONS, GUILD_VERIFICATION_LEVELS
from ...utils.helpers import CleanEmbed, TimeConverters
from ...utils.config import Config


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="status")
    @commands.guild_only()
    async def _status(self, ctx: commands.Context) -> None:
        embed = CleanEmbed(
            author_text="Freddy statistics",
            thumbnail_url=self.bot.user.avatar_url,
            fields=[
                {"name": "Total Servers", "value": len(self.bot.guilds), "inline": True},
                {"name": "Total Users", "value": len(self.bot.users), "inline": True},
                {"name": "Total Channels", "value": len([c.channels for c in self.bot.guilds]), "inline": True},
                {"name": "Uptime", "value": TimeConverters.seconds_to_humanised((datetime.utcnow() - self.bot.uptime).total_seconds())}
            ]
        )

        await ctx.send(embed=embed)

    @commands.command(name="botinfo")
    @commands.guild_only()
    async def botinfo(self, ctx: commands.Context) -> None:
        """Shows information about Freddy"""

        embed = CleanEmbed(
            author_text="About Freddy",
            description=f"Freddy is a powerful multi-purpose bot, developed and designed with ease of use in mind. "
                        f"Created {(datetime.utcnow() - self.bot.user.created_at).days} days ago, he has been providing "
                        f"value to many guilds for a long time.",
            thumbnail_url=self.bot.user.avatar_url,
            fields=[
                {"name": "Commands", "value": f"{len(self.bot.commands)} public commands", "inline": True},
                {"name": "Maintainment", "value": "Developed and designed by Harry", "inline": True},
                {"name": "Invite Freddy", "value": "Invite here", "inline": True},
                {"name": "Timeline", "value":
                    "~~-~~**1**~~------~~**2**~~-------~~**3**~~------------------~~**4**~~-----------~~**5**~~-~~ \n\n"
                    "**1** - " + self.bot.user.created_at.strftime("%B %Y") + " - Freddy was created \n"
                    "**2** - November 2019 - Development was paused \n"
                    "**3** - January 2020 - Development resumed and Freddy grew rapidly \n"
                    "**4** - December 2020 - Freddy's development stopped \n"
                    "**5** - May 2021 - In process of re-designing and bot verification"
                 }
            ]
        )

        await ctx.send(embed=embed)

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
    async def _spotify(self, ctx: commands.Context, member: Member = None) -> Union[commands.Context, None]:
        """Shows what a member is listening to on Spotify, if applicable"""

        if member is None:
            member = ctx.author

        if member.activities is not None:
            for activity in member.activities:
                if isinstance(activity, Spotify):
                    embed = CleanEmbed(
                        author_text=f"{member.name}#{member.discriminator} is listening to Spotify",
                        thumbnail_url=activity.album_cover_url,
                        description=f"{activity.title} on {activity.album} \n**By** {', '.join(activity.artists)} \n\n"
                                    f"[{Config.SPOTIFY_EMOJI_STR} Listen to {activity.title} on Spotify](https://open.spotify.com/track/{activity.track_id})"
                    )

                    return await ctx.send(embed=embed)

        await ctx.send(f"{member.name}#{member.discriminator} isn't currently listening to Spotify.")


def setup(bot):
    bot.add_cog(Information(bot))


from discord.ext import commands

from ...utils.helpers import CleanEmbed


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="dog", aliases=["woof", "doggo"])
    @commands.guild_only()
    async def _dog(self, ctx: commands.Context) -> None:
        """Displays a random dog image inside of an embed"""

        async with ctx.channel.typing():
            async with self.bot.session.get("https://dog.ceo/api/breeds/image/random") as res:
                image = (await res.json())["message"]

        embed = CleanEmbed(
            author_url=image,
            author_text="Here's a doggo 🐕",
            image_url=image,
        )

        await ctx.send(embed=embed)

    @commands.command(name="cat", aliases=["meow"])
    @commands.guild_only()
    async def _cat(self, ctx: commands.Context) -> None:
        """Displays a random cat image inside of an embed"""

        async with ctx.channel.typing():
            async with self.bot.session.get("https://aws.random.cat/meow") as res:
                image = (await res.json())["file"]

        embed = CleanEmbed(
            author_url=image,
            author_text="Here's a cat 🐱",
            image_url=image,
        )

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))


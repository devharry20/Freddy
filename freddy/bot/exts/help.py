from discord.ext import commands

from ...utils.helpers import CleanEmbed


class HelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping) -> None:
        """Sends a help embed displaying all of Freddy's commands"""

        embed = CleanEmbed(
            author_text="Freddy Help",
            thumbnail_url="https://cdn.discordapp.com/avatars/842450701920895036/5acd4c6d73cf152f25d242f89edc2288.png?size=256"
        )

        for cog, _cmds in mapping.items():
            filtered_commands = await self.filter_commands(_cmds, sort=True)

            if [c.name for c in filtered_commands][0] != "help":
                cog_name = getattr(cog, "qualified_name", "No Category")

                cmds = []
                for cmd in filtered_commands:
                    cmd_params = " ".join(f"[{c}]" for c in cmd.clean_params.keys()) if len(cmd.clean_params.keys()) > 0 else ""
                    cmds.append(f"`f!{cmd.name}`" if not cmd_params else f"`f!{cmd.name} {cmd_params}`")

                embed.add_field(name=cog_name, value="\n".join(cmds), inline=False)

        await self.get_destination().send(embed=embed)

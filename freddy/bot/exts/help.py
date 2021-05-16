from discord.ext import commands

from ...utils.helpers import CleanEmbed


class HelpCommand(commands.HelpCommand):
    def get_command_usage(self, command: commands.Command) -> str:
        """Returns a string containing the command usage and any parameters it takes"""

        params = " ".join(f"[{c}]" for c in command.clean_params.keys()) if len(command.clean_params.keys()) > 0 else ""

        return f"`f!{command.name}`" if not params else f"`f!{command.name} {params}`"

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
                    cmds.append(self.get_command_usage(cmd))

                embed.add_field(name=cog_name, value="\n".join(cmds), inline=False)

        await self.get_destination().send(embed=embed)

    async def send_command_help(self, command: commands.Command) -> None:
        """Sends a help embed displaying command specific information"""

        embed = CleanEmbed(
            author_text=f"Freddy Help: {command.name}",
            description=command.callback.__doc__,
            fields=[
                {"name": "Expected Usage", "value": self.get_command_usage(command), "inline": True}
            ]
        )

        await self.get_destination().send(embed=embed)

    async def send_error_message(self, error: str) -> None:
        """Returns immediately to prevent any error message being sent"""

        return


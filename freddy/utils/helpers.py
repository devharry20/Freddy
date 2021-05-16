from discord import Embed

from ..utils.config import Config

import time


class CleanEmbed(Embed):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = kwargs.get('title') or self.Empty
        self.description = kwargs.get('description') or self.Empty
        self.colour = kwargs.get('colour') or Config.DEFAULT_COLOUR

        if kwargs.get('author_text') is not None:
            self.set_author(name=kwargs.get('author_text') or self.Empty,
                            icon_url=kwargs.get('author_image') or self.Empty,
                            url=kwargs.get('author_url') or self.Empty)

        self.set_thumbnail(url=kwargs.get('thumbnail_url') or self.Empty)
        self.set_image(url=kwargs.get('image_url') or self.Empty)
        self.set_footer(text=kwargs.get('footer_text') or self.Empty, icon_url=kwargs.get('footer_text') or self.Empty)
        self.timestamp = kwargs.get('timestamp') or self.Empty

        if kwargs.get('fields') is not None:
            for field in kwargs.get('fields'):
                if 'inline' not in field:
                    field['inline'] = False

                self.add_field(**field)


class TimeConverters:
    @staticmethod
    def seconds_to_humanised(delay: int) -> str:
        """A hacky function to convert seconds to a human readable format"""

        ty_res = time.gmtime(delay)
        hours = time.strftime("%H", ty_res)
        minutes = time.strftime("%M", ty_res)
        seconds = time.strftime("%S", ty_res)

        humanised = ""

        if int(hours) > 0:
            humanised += f"{hours} hour " if int(hours) == 1 else f"{hours} hours "
        if int(minutes) > 0:
            humanised += f"{minutes} minute " if int(minutes) == 1 else f"{minutes} minutes "
        if int(seconds) > 0:
            humanised += f"{seconds} second " if int(seconds) == 1 else f"{seconds} seconds "

        return f"{humanised.rstrip()}."

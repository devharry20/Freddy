from discord import Embed

from datetime import datetime


class CleanEmbed(Embed):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.title = kwargs.get('title') or self.Empty
        self.description = kwargs.get('description') or self.Empty
        self.colour = kwargs.get('colour') or 0xF2C572

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

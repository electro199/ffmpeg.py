import os
from .base import BaseFilter
from .mixins.enable import TimelineEditingMixin


class Text(BaseFilter, TimelineEditingMixin):
    def __init__(
        self, text, y, x, fontsize=16, color="white", fontname="arial.ttf", **kwargs
    ):
        super().__init__("drawtext")
        self.flags = {
            "text": "'" + text + "'",
            "fontfile": self.get_fontfile(fontname),
            "fontsize": fontsize,
            "x": x,
            "y": y,
            "fontcolor": color,
        }
        self.flags.update(kwargs)

    def get_fontfile(self, fontname):
        return (
            r"C\\://Windows/Fonts/" + fontname
            if os.name == "nt"
            else "/usr/share/fonts/truetype/freefont/" + fontname
        )
    #TODO add text escaping 
    # def text_escape(self, text:str):
    #     return text.replace()
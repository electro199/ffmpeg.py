from typing import Optional
from .base import BaseFilter


class Subtitles(BaseFilter):
    """
    Draw subtitles on top of input video using the libass library.
    """

    def __init__(
        self,
        filename: str,
        width: Optional[int] = None,
        height: Optional[int] = None,
        fontsdir: Optional[str] = None,
        alpha: Optional[bool] = None,
        charenc: Optional[str] = None,
        stream_index: Optional[int] = None,
        force_style: Optional[str] = None,
        wrap_unicode: Optional[bool] = None,
    ):
        super().__init__("subtitles")

        original_size = None
        if width and height:
            original_size = f"{width}x{height}"

        self.flags = {
            "filename": self.escape_path(filename),
            "original_size": original_size,
            "fontsdir": self.escape_path(fontsdir),
            "alpha": alpha,
            "charenc": charenc,
            "stream_index": stream_index,
            "force_style": force_style,
            "wrap_unicode": wrap_unicode,
        }

    def escape_path(self, path):
        """
        no backslash allowed
        `:` must be escaped
        """
        return f"'{path}'".replace("\\", "/").replace(":", "\\:")

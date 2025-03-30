from typing import Literal, Optional
from .base_input import BaseInput
from .streams import StreamSpecifier
from ..ffprobe.ffprobe import ffprobe


class VideoFile(BaseInput):
    def __init__(self, filepath: str) -> None:
        super().__init__()
        self.filepath = filepath

    def build_input_flags(self) -> list[str]:
        command = self.build()
        command.extend(["-i", self.filepath])
        return command

    def subclip(self, start: float, end: float):
        self.flags.update((("ss", start), ("t", end)))
        return self

    def __repr__(self) -> str:
        return f"<VideoFile filepath={self.filepath}>"

    @classmethod
    def from_imagefile(cls, imgpath: str, duration: float, fps: int):
        c = cls(imgpath)
        c.flags["loop"] = 1
        c.flags["t"] = duration
        c.flags["framerate"] = fps
        return c

    @property
    def audio(self) -> StreamSpecifier:
        """
        Access Audio stream of the media
        """
        return StreamSpecifier(self, stream_name="a")

    @property
    def video(self) -> StreamSpecifier:
        """
        Access Video stream of the media
        """
        return StreamSpecifier(self, stream_name="v")

    @property
    def subtitle(self) -> StreamSpecifier:
        """
        Access Subtitle stream of the media
        """
        return StreamSpecifier(self, stream_name="s")

    def get_stream(
        self,
        stream_index: int,
        stream_name: Optional[Literal["a", "v", "s"]] = None,
    ) -> StreamSpecifier:
        return StreamSpecifier(self, stream_name=stream_name, stream_index=stream_index)

    def get_size(self):
        data = ffprobe(
            self.filepath,
            (
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height",
            ),
        )["streams"][0]
        return data["width"], data["height"]

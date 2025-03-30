from typing import Literal, Optional
from .options.file_input_option import FileInputOptions
from .base_input import BaseInput
from .streams import StreamSpecifier


class InputFile(BaseInput):
    """
    General Input for FFMPEG backend You can use custom flags
    """

    def __init__(
        self, filepath: str, options: Optional[FileInputOptions] = None
    ) -> None:
        self.filepath = filepath
        self.options = options

    def build_input_flags(self) -> list[str]:
        command = []
        if self.options:
            command.extend(self.options.build())
        command.extend(["-i", self.filepath])
        return command

    def __repr__(self) -> str:
        return f"<InputFile {self.filepath}>"

    @property
    def audio(self):
        return StreamSpecifier(self, stream_name="a")

    @property
    def video(self):
        return StreamSpecifier(self, stream_name="v")

    def get_stream(
        self,
        stream_index: int,
        stream_name: Optional[Literal["a", "v", "s"]] = None,
    ) -> StreamSpecifier:
        return StreamSpecifier(self, stream_name=stream_name, stream_index=stream_index)

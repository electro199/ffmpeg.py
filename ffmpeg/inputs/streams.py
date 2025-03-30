from typing import Literal, Optional


class StreamSpecifier:
    """
    Used specify in ffmpeg command
    
    ffmpeg docs : https://ffmpeg.org/ffmpeg.html#toc-Automatic-stream-selection
    """

    __slots__ = (
        "parent",
        "stream_index",
        "stream_name",
        "output_number",
    )

    def __init__(
        self,
        parent,
        output_index=0,
        stream_index: Optional[int] = None,
        stream_name: Optional[Literal["a", "v", "s"]] = None,
    ) -> None:
        self.parent = parent
        self.stream_index = stream_index
        self.stream_name = stream_name
        self.output_number = output_index

    def build_stream_str(self):
        s = ""
        if self.stream_name:
            s += ":" + str(self.stream_name)

        if self.stream_index is not None:
            s += ":" + str(self.stream_index)

        return s

    def get_outputs(self):
        return StreamSpecifier(self)

from typing import Iterable, Literal, Optional
from ..inputs import BaseInput, StreamSpecifier

#TODO stream_type can be inferred from input node
class Map:
    """
    Represents a single input stream mapping for an FFmpeg output.

    This class encapsulates an input source (`BaseInput` or `StreamSpecifier`) along with
    optional stream type and FFmpeg-specific flags that will be applied during the mapping.

    Args:
        node (BaseInput | StreamSpecifier): The input source to map (either a full input or a specific stream).
        suffix_flags (Optional[dict], optional): Additional flags to apply **after** the `-map` option.
        stream_type (Optional[Literal["a", "v", "s"]], optional): A shortcut to specify audio ('a'), video ('v'), or subtitle ('s') streams.
        **flags: Additional key-value FFmpeg flags applied directly to the mapping.

    Example:
        ```python
        Map(VideoFile("in.mp4").video, stream_type="v", codec="libx264")
        ```
    """
    def __init__(
        self,
        node: BaseInput | StreamSpecifier,
        suffix_flags: Optional[dict] = None,
        stream_type: Optional[Literal["a", "v", "s"]] = None,
        **flags,
    ) -> None:
        self.node = node
        self.stream_type = stream_type
        self.suffix_flags = {}
        if suffix_flags:
            self.suffix_flags = {**suffix_flags}
        self.flags = {**flags}


class OutFile:
    """
    Represents an FFmpeg output configuration.

    This class wraps multiple mapped inputs (as `Map` objects), the output file path,
    and any output flags.

    Args:
        maps (Iterable[Map]): List of `Map` objects defining which input streams to include.
        path (str): Output file path (e.g., `"out.mp4"`).
        **kvflags: Additional key-value FFmpeg output flags (e.g., `crf=23`, `preset="fast"`).

    Example:
        ```python
        OutFile(
            maps=[
                Map(VideoFile("input.mp4").video),
                Map(VideoFile("input.mp4").audio)
            ],
            path="output.mp4",
            crf=23,
            preset="fast"
        )
        ```
    """
    def __init__(self, maps: Iterable[Map], path, **kvflags) -> None:
        self.maps, self.path, self.kvflags = maps, path, kvflags

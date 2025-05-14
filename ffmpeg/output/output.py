from typing import Iterable, Literal, Optional
from ..inputs import BaseInput, StreamSpecifier


# TODO stream_type can be inferred from input node
class Map:
    def __init__(
        self,
        node: BaseInput | StreamSpecifier,
        suffix_flags: Optional[dict] = None,
        stream_type: Optional[Literal["a", "v", "s", "d", "t", "V"]] = None,
        **flags,
    ) -> None:
        """
        Represents a single input stream mapping for an FFmpeg output.

        This class encapsulates an input source (`BaseInput` or `StreamSpecifier`) along with
        optional stream type and FFmpeg-specific flags that will be applied during the mapping.

        Args:
            node (BaseInput | StreamSpecifier): The input source to map (either a full input or a specific stream).
            suffix_flags (Optional[dict], optional): Additional flags to apply **after** the `-map` option.
            stream_type (Optional[Literal["a", "v", "s", "d", "t", "V"]], optional): A shortcut to specify audio ('a'), video ('v'), or subtitle ('s') streams.
            **flags: Additional key-value FFmpeg flags applied directly to the mapping.

        Example:
            ```python
            Map(VideoFile("in.mp4").video, stream_type="v", codec="libx264")
            ```
        """
        self.node = node
        self.stream_type = stream_type
        self.suffix_flags = {}
        if suffix_flags:
            self.suffix_flags = {**suffix_flags}
        self.flags = {**flags}

    def build(self, map_index):

        flags = []
        # use stream type like foo:v
        stream_type_specfier = f":{self.stream_type}" if self.stream_type else ""

        for k, v in self.suffix_flags.items():
            flags.append(f"-{k}{stream_type_specfier}:{map_index}")
            flags.append(str(v))

        for k, v in self.flags.items():
            flags.append(f"-{k}")
            flags.append(str(v))

        return flags


class OutFile:
    def __init__(
        self, maps: Iterable[Map], path, *, options: Optional[dict] = None, **kvflags
    ) -> None:
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
        self.maps, self.path, self.kvflags = maps, path, kvflags

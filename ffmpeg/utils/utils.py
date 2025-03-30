from typing import Iterable
from ..inputs import BaseInput, StreamSpecifier

from ..ffmpeg import FFmpeg
from ..models.output import Map


def export(*nodes:BaseInput | StreamSpecifier, path: str) -> FFmpeg:
    """
    Exports a clip by processing the given input nodes and saving the output to the specified path.

    Args:
        nodes: One or more input nodes representing media sources.
        path: The output file path where the exported clip will be saved.

    Returns:
        FFmpeg: An FFmpeg command instance configured with the given inputs and output path.
    """
    return FFmpeg().output(*(Map(node) for node in nodes), path=path)

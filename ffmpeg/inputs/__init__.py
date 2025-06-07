from .file_input import InputFile
from .base_input import BaseInput
from .streams import StreamSpecifier
from .video import VideoFile
from .audio import AudioFile
from .image import ImageFile
from .virtual_video import VirtualVideo

from .options.file_input_option import FileInputOptions

__all__ = [
    "VideoFile",
    "AudioFile",
    "ImageFile",
    "VirtualVideo",
    "InputFile",
    "FileInputOptions",
    "StreamSpecifier",
    "BaseInput",
]

"""
FFmpeg Wrapper for Python

This module provides a Pythonic interface to FFmpeg, allowing users to construct and execute FFmpeg commands programmatically.
It simplifies video and audio processing tasks such as format conversion, filtering, and transcoding.


Requirements:
- FFmpeg must be installed and accessible via the system path.

"""

from . import inputs, filters, exception, ffplay, ffprobe
from .models import output

from .inputs import InputFile, FileInputOptions, VideoFile
from .filters import apply, apply2
from .models.output import Map, OutFile
from .ffmpeg import FFmpeg, export
from .exception import FFmpegException, FFprobeException


import logging

logger = logging.getLogger("ffmpeg")


__version__ = "0.0.5"

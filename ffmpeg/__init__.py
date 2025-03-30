"""
FFmpeg Wrapper for Python

This module provides a Pythonic interface to FFmpeg, allowing users to construct and execute FFmpeg commands programmatically.
It simplifies video and audio processing tasks such as format conversion, filtering, and trancoding.


Requirements:
- FFmpeg must be installed and accessible via the system path.

"""

from . import inputs
from . import filters
from .models import output

from .ffmpeg import FFmpeg
from .exception import FFmpegException, FFprobeException


from .utils.utils import export
from .ffplay import ffplay
from .ffprobe import ffprobe

import logging

logger = logging.getLogger("ffmpeg")


__version__ = "0.0.4"

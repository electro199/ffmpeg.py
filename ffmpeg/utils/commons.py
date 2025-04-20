"""
common functions used by ffmpeg.py feel free to use them!

"""

from typing import Any


def wrap_quotes(text: str) -> str:
    return '"' + text + '"'


def wrap_sqrtbrkt(text: str) -> str:
    return "[" + str(text) + "]"


def parse_value(value):
    """Convert FFmpeg progress values to appropriate data types."""
    if value.isdigit():
        return int(value)
    try:
        return float(value)
    except ValueError:
        return value


def build_flags(kwflags: dict[str, Any]) -> list[str]:
    """Generate flags"""
    flags = []

    for k, v in kwflags.items():
        flags.append(f"-{k}")
        flags.append(str(v))

    return flags

import subprocess
from typing import Optional, Union


def ffplay(
    file_path: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    fullscreen: bool = False,
    disable_audio: bool = False,
    disable_video: bool = False,
    disable_subtitles: bool = False,
    seek_position: Optional[Union[int, float, str]] = None,
    duration: Optional[Union[int, float]] = None,
    seek_by_bytes: bool = False,
    seek_interval: Optional[Union[int, float]] = None,
    nodisp: bool = False,
    noborder: bool = False,
    alwaysontop: bool = False,
    volume: Optional[int] = None,
    force_format: Optional[str] = None,
    window_title: Optional[str] = None,
    left: Optional[int] = None,
    top: Optional[int] = None,
    loop: Optional[int] = None,
    showmode: Optional[int] = None,
    video_filter: Optional[str] = None,
    audio_filter: Optional[str] = None,
    autoexit: bool = False,
    fbuf: bool = False,
    sync: Optional[str] = None,
    fast: bool = False,
    stats: bool = False,
    drp: bool = False,
    fflags: Optional[str] = None,
    vf: Optional[str] = None,
    af: Optional[str] = None,
    framedrop: bool = False,
) -> None:
    """
    Run ffplay to play the specified media file with customizable options.
    """
    args = locals()
    options = []

    # Special case for width and height
    if args["width"] and args["height"]:
        options.append(f"-x {args['width']} -y {args['height']}")

    # Boolean flags (enabled if True)
    flag_map = {
        "fullscreen": "-fs",
        "disable_audio": "-an",
        "disable_video": "-vn",
        "disable_subtitles": "-sn",
        "seek_by_bytes": "-bytes",
        "nodisp": "-nodisp",
        "noborder": "-noborder",
        "alwaysontop": "-alwaysontop",
        "autoexit": "-autoexit",
        "infbuf": "-infbuf",
        "fast": "-fast",
        "stats": "-stats",
        "drp": "-drp",
        "framedrop": "-framedrop",
    }

    # Key-value flags
    value_map = {
        "seek_position": "-ss",
        "duration": "-t",
        "seek_interval": "-seek_interval",
        "volume": "-volume",
        "force_format": "-f",
        "window_title": "-window_title",
        "left": "-left",
        "top": "-top",
        "loop": "-loop",
        "showmode": "-showmode",
        "video_filter": "-vf",
        "audio_filter": "-af",
        "sync": "-sync",
        "fflags": "-fflags",
        "vf": "-vf",
        "af": "-af",
    }

    for key, flag in flag_map.items():
        if args.get(key):
            options.append(flag)

    for key, flag in value_map.items():
        val = args.get(key)
        if val is not None:
            if key == "window_title":
                options.append(f'{flag} "{val}"')
            else:
                options.append(f"{flag} {val}")

    cmd = f'ffplay -v error {" ".join(options)} "{file_path}"'
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"Error running ffplay: {e}")

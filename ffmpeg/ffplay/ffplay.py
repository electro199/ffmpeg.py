
import subprocess

def ffplay(file_path, width=None, height=None, fullscreen=False, disable_audio=False, disable_video=False,
           disable_subtitles=False, seek_position=None, duration=None, seek_by_bytes=False, seek_interval=None,
           nodisp=False, noborder=False, alwaysontop=False, volume=None, force_format=None, window_title=None,
           left=None, top=None, loop=None, showmode=None, video_filter=None, audio_filter=None):
    """
    Run ffplay to play the specified media file with customizable options.
    """
    options = []
    if width and height:
        options.append(f"-x {width} -y {height}")
    if fullscreen:
        options.append("-fs")
    if disable_audio:
        options.append("-an")
    if disable_video:
        options.append("-vn")
    if disable_subtitles:
        options.append("-sn")
    if seek_position:
        options.append(f"-ss {seek_position}")
    if duration:
        options.append(f"-t {duration}")
    if seek_by_bytes:
        options.append("-bytes")
    if seek_interval:
        options.append(f"-seek_interval {seek_interval}")
    if nodisp:
        options.append("-nodisp")
    if noborder:
        options.append("-noborder")
    if alwaysontop:
        options.append("-alwaysontop")
    if volume is not None:
        options.append(f"-volume {volume}")
    if force_format:
        options.append(f"-f {force_format}")
    if window_title:
        options.append(f"-window_title \"{window_title}\"")
    if left is not None:
        options.append(f"-left {left}")
    if top is not None:
        options.append(f"-top {top}")
    if loop is not None:
        options.append(f"-loop {loop}")
    if showmode:
        options.append(f"-showmode {showmode}")
    if video_filter:
        options.append(f"-vf {video_filter}")
    if audio_filter:
        options.append(f"-af {audio_filter}")
    
    cmd = f"ffplay {' '.join(options)} \"{file_path}\""
    try:
        subprocess.run(cmd, shell=True)
    except Exception as e:
        print(f"Error running ffplay: {e}")

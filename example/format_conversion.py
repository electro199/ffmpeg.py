from ffmpeg.inputs import InputFile
from ffmpeg import export


export(
    InputFile(r"video.mp4"),
    path="out.mkv",
).run()

from ffmpeg.inputs import VideoFile
from ffmpeg import export


export(
    VideoFile("video.mp4").video,
    VideoFile("video1.mp4").audio,
    path="out.mp4",
).run()

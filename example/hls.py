from pprint import pprint
from ffmpeg.filters import Scale, Split, apply, apply2
from ffmpeg.inputs import InputFile, FileInputOptions
from ffmpeg.ffmpeg import FFmpeg
from ffmpeg.models.output import Map

# Input video
input_video = InputFile(
    r"in.mkv",  # put input here
    FileInputOptions(re=True, duration=10),
)

# Split video into three streams
split_video = apply2(Split(3), input_video.video)
v1, v2, v3 = split_video

# Apply scaling filters
v2_scaled = apply(Scale(1280, 720), v2)
v3_scaled = apply(Scale(640, 360), v3)

# Export the final output with different bitrate and HLS settings
export = FFmpeg().output(
    Map(
        v1,
        stream_type="v",
        c="libx264",
        b="5M",
        maxrate="5M",
        minrate="5M",
        bufsize="10M",
        preset="slow",
        flags={
            "g": 48,
            "sc_threshold": 0,
            "keyint_min": 48,
            "x264-params": "nal-hrd=cbr:force-cfr=1",
        },
    ),
    Map(
        v2_scaled,
        stream_type="v",
        c="libx264",
        b="3M",
        maxrate="3M",
        minrate="3M",
        bufsize="3M",
        preset="slow",
        flags={
            "g": 48,
            "sc_threshold": 0,
            "keyint_min": 48,
            "x264-params": "nal-hrd=cbr:force-cfr=1",
        },
    ),
    Map(
        v3_scaled,
        stream_type="v",
        c="libx264",
        b="1M",
        maxrate="1M",
        minrate="1M",
        bufsize="1M",
        preset="slow",
        flags={
            "g": 48,
            "sc_threshold": 0,
            "keyint_min": 48,
            "x264-params": "nal-hrd=cbr:force-cfr=1",
        },
    ),
    Map(input_video.get_stream(0, "a"), c="aac", b="96k", ac=2),  # audio 1
    Map(input_video.get_stream(1, "a"), c="aac", b="96k", ac=2),  # audio 2
    format="hls",
    hls_time=2,
    hls_playlist_type="vod",
    hls_flags="independent_segments",
    hls_segment_type="mpegts",
    hls_segment_filename="output/stream_%v/data%02d.ts",
    master_pl_name="master.m3u8",
    var_stream_map="a:0,agroup:audio,default:yes,language:en,name:en a:1,agroup:audio,default:yes,language:en,name:other v:0,agroup:audio,name:1080 v:1,agroup:audio,name:720 v:2,agroup:audio,name:360",
    path="output/stream_%v/stream.m3u8",
)

# print(" ".join(export.compile()))
print(export.run())

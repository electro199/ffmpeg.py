This library provides a Pythonic interface to FFmpeg, making it easier to handle video and audio processing.
Below is a quick guide to get you started using FFmpeg.py with minimal code.

---

FFmpeg.py comes with an easy-to-use `export` function that export the single output with multiple stream.

Here quickly combine audio and video from files and output them to a single file.

```py
from ffmpeg.inputs import VideoFile
from ffmpeg import export

export(
    VideoFile("video1.mp4").video,  # Video stream from video.mp4
    VideoFile("video2.mp4").audio,  # Audio stream from video1.mp4
    path="out.mp4",  # Output path
).run()

# ffmpeg ... -i video1.mp4 -i video2.mp4 -map 0:v -map 1:a out.mp4
```

This code extracts the **video** from `video.mp4` and the **audio** from `video1.mp4`, then exports them into a single output file `out.mp4`.

Which is same as Using `FFmpeg()` with `Map` but in this way you can add flags per `Map` like encoding.

```py
from ffmpeg.inputs import VideoFile
from ffmpeg import FFmpeg, Map

FFmpeg().output(
    Map(VideoFile("video.mp4").video),  # Map video stream from video.mp4
    Map(VideoFile("video1.mp4").audio),  # Map audio stream from video1.mp4
    path="out.mp4",  # Output path
).run()
# ffmpeg ... -i video.mp4 -i video1.mp4 -map 0:v -map 1:a out.mp4
```
!!! tip
    This method provides a more **explicit** control flow where each stream is mapped individually. you can provide flags for `-map` context with both stream suffixed flag or without. 

---

## Example

Lets make a video from a image with audio with

```py
from ffmpeg.ffmpeg import FFmpeg
from ffmpeg.inputs import FileInputOptions, InputFile
from ffmpeg.models.output import Map

# set options
clip = InputFile(
    "image.png",
    FileInputOptions(loop=True, duration=5, frame_rate=60),
)
audio = InputFile(
    "audio.mp3",
    FileInputOptions(duration=5),
)

# run command
ffmpeg = (
    FFmpeg().output(Map(clip), Map(audio), path="out.mp4").run()
)

# ffmpeg ... -t 5 -r 60 -loop 1 -i image.png -t 5 -i audio.mp3 -map 0 -map 1 out.mp4
```

Here we are using `InputFile` it is for generic input which are support by FFmpeg like path or url in combination with `FileInputOptions`
this provide useful flags that are applied to input in ffmpeg command.

The above code is easy to understand which works like:

- `loop=True` will make a infinite loop
- we set a `duration` so infinite loop can end
- then set `frame_rate` at 60

# Filters
Filters can be used with  [`apply`](/api/#ffmpeg.filters.apply) or [`apply2`](/api/#ffmpeg.filters.apply2), apply2 is for multi output filters like Split and Concat.

Usage:

```py
clip = InputFile("image.png")
clip_scaled = apply(Scale(1000, 1000), clip)

```

Lets scale the image and then use it

At end we make a FFmpeg and add a output with two stream mapping. The `Map` add stream(s) to a output file in this way we can add multiple streams to one output, for more complex use case see Advance Usage like Filtering, Multiple outputs or what is progress_callback.

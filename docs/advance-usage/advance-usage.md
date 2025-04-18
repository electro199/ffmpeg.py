Lets see how everything works in FFmpeg.py

# Input 
The ffmpeg takes input in `[-key value -i path]`, ffmpeg.py will make a input with `InputFile` or `VideoFile`. Both of them are does same thing but with VideoFile it comes with addition features like:

- **subclip** that sets `-ss` and `-t`  for seek start and duration repectively
- **from_imagefile**  that sets `-t`  for duration and enable `loop`.
- **general streams** like video, audio and subtitles that corresponds to `stream_name:v:n`/`stream_name:a:n`/`stream_name:s:n` in both filter and map context in command.


# Global flags
Global flags are used change settings for whole runtime, you can use `add_global_flag` to set custom flags, These flags are automatic added duration command generation in `FFmpeg.compile()`:

- `-y` or `-n` to set overwrite outfile 
- `-loglevel error` to only read errors
- `-hide_banner` to avoid extra pipe writes and cleaner output.

## Usage
The `add_global_flag` take raw flags example as:
```
FFmpeg().add_global_flag("-recast_media")

## Results ffmpeg -recast_media -i ....
```

# Filters
Filters are way the ffmpeg allow media to be manipulated, ffmpeg.py use [`apply`](ffmpeg.filters.apply)
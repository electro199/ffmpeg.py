# FFmpeg.py

FFmpeg Wrapper for Python
This module provides a Pythonic interface to FFmpeg, allowing users to construct and execute FFmpeg commands programmatically.
It simplifies video and audio processing tasks such as format conversion, filtering, and transcoding.

## Installation

### Using Package Manager
```sh
pip install git+https://github.com/electro199/ffmpeg.py.git
```

### Install FFmpeg

This project does not install ffmpeg utility automatically.

#### Windows
Using winget:
```sh
winget install --id=Gyan.FFmpeg  -e
```

or download and install FFmpeg from [FFmpeg official website](https://ffmpeg.org/download.html):
1. Download the latest FFmpeg build from [here](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the archive and add the `bin` directory to your system `PATH`.

#### macOS
Using Homebrew:
```sh
brew install ffmpeg
```

#### Linux
For Debian/Ubuntu:
```sh
sudo apt update && sudo apt install ffmpeg
```
Verify installation:
```sh
ffmpeg -version
```

## Usage

For simple media conversion :

```py
from ffmpeg.inputs import VideoFile
from ffmpeg import export

clip = VideoFile("video.mp4")

export(
   clip,
   path="out.mkv",
).run()

```
## Advaced Usage
Lets use ffmpeg powerfull features to scale and overlay.

```py
from ffmpeg.ffmpeg import FFmpeg
from ffmpeg.inputs import InputFile, FileInputOptions
from ffmpeg.filters import apply, Scale, OverlayFilter
from ffmpeg.models.output import Map

# set options
clip = InputFile("video.mp4", FileInputOptions(duration=10))
overlay = InputFile("overlay.png")

# apply scale filter on clip
upscaled_clip = apply(Scale(1440, 1920), clip)

# apply scale filter on overlay
overlay = apply(Scale(100, 100), overlay)

# apply overlay filter with overlay on upscaled_clip
upscaled_clip = apply(OverlayFilter(overlay, x=0, y=10), clip)

# run command 
ffmpeg = FFmpeg().output(Map(upscaled_clip), path="out.mp4").run(progress_callback=print)
```

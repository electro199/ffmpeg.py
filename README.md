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

#### Windows
Using winget:
```sh
winget install --id=Gyan.FFmpeg  -e
```

or download and install FFmpeg from [FFmpeg official website](https://ffmpeg.org/download.html):
1. Download the latest FFmpeg build from [here](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the archive and add the `bin` directory to your system `PATH`.
3. Verify installation:
   ```sh
   ffmpeg -version
   ```

#### macOS
Using Homebrew:
```sh
brew install ffmpeg
```
Verify installation:
```sh
ffmpeg -version
```

#### Linux
For Debian/Ubuntu:
```sh
sudo apt update && sudo apt install ffmpeg
```

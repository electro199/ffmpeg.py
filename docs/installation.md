### Install Library
```sh
pip install git+https://github.com/electro199/ffmpeg.py.git
```

---


!!! note
    This project does not install ffmpeg utility automatically. 

## Install FFmpeg
Use any of these methods:

#### Windows
Using winget:
```sh
winget install --id=Gyan.FFmpeg  -e
```

or download and install FFmpeg from [FFmpeg official website](https://ffmpeg.org/download.html):

1. Download the latest FFmpeg build from [here](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the archive and add the `bin` directory to your system `PATH`.

#### Linux
For Debian/Ubuntu:
```sh
sudo apt install ffmpeg
```

#### MacOS
Using Homebrew:
```sh
brew install ffmpeg
```


## Verify installation
```sh
ffmpeg -version
```

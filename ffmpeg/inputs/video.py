from typing import Literal, Optional
from .base_input import BaseInput
from .streams import StreamSpecifier
from ..ffprobe.ffprobe import ffprobe


class VideoFile(BaseInput):
    """
    A class representing a video file that can be processed with FFmpeg.

    This class provides methods for interacting with a video file, such as 
    building FFmpeg input flags, extracting streams (audio, video, subtitles),
    creating subclips, and retrieving the video file's resolution.
    """

    def __init__(self, filepath: str) -> None:
        """
        Initializes the VideoFile object with the specified file path.

        Args:
            filepath (str): The path to the video file to be processed.
        """
        super().__init__()
        self.filepath = filepath
    @property
    def audio(self) -> StreamSpecifier:
        """
        Access the audio stream of the video file.

        Returns:
            StreamSpecifier: A StreamSpecifier object for the audio stream.
        """
        return StreamSpecifier(self, stream_name="a")

    @property
    def video(self) -> StreamSpecifier:
        """
        Access the video stream of the video file.

        Returns:
            StreamSpecifier: A StreamSpecifier object for the video stream.
        """
        return StreamSpecifier(self, stream_name="v")

    @property
    def subtitle(self) -> StreamSpecifier:
        """
        Access the subtitle stream of the video file.

        Returns:
            StreamSpecifier: A StreamSpecifier object for the subtitle stream.
        """
        return StreamSpecifier(self, stream_name="s")

    def get_stream(
        self,
        stream_index: int,
        stream_name: Optional[Literal["a", "v", "s"]] = None,
    ) -> StreamSpecifier:
        """
        Get a specific stream from the video file by index and/or stream name. 
        
        Example:
            You get 2nd audio stream from video like this. 
            ```python 
            clip.get_stream(stream_index=1,stream_name="a")
            ```
            
        Args:
            stream_index (int): The index of the stream (e.g., 0 for the first stream).
            stream_name (Optional[Literal["a", "v", "s"]]): The name of the stream 
                to retrieve ("a" for audio, "v" for video, "s" for subtitles). 
                If not provided, retrieves the stream by index.

        Returns:
            StreamSpecifier: A StreamSpecifier object for the requested stream.
        """
        return StreamSpecifier(self, stream_name=stream_name, stream_index=stream_index)

    def build_input_flags(self) -> list[str]:
        """
        Builds the FFmpeg input flags for the video file.

        This method constructs the FFmpeg command line input flags to specify 
        the video file to be processed.

        Returns:
            list[str]: A list of input flags for FFmpeg, including the file path.
        """
        command = self.build()
        command.extend(["-i", self.filepath])
        return command

    def subclip(self, start: float, end: float):
        """
        Defines a subclip from the video file by setting the start and end times.

        Args:
            start (float): The start time of the subclip in seconds.
            end (float): The end time of the subclip in seconds.

        Returns:
            VideoFile: The updated VideoFile object with the subclip flags set.
        """
        self.flags.update((("ss", start), ("t", end)))
        return self

    @classmethod
    def from_imagefile(cls, imgpath: str, duration: float, fps: int):
        """
        Creates a VideoFile object from an image file, looping it for the given 
        duration and setting the frame rate.

        Args:
            imgpath (str): The path to the image file to use as a video.
            duration (float): The duration of the video in seconds.
            fps (int): The frame rate of the video.

        Returns:
            VideoFile: A VideoFile object created from the image file.
        """
        c = cls(imgpath)
        c.flags["loop"] = 1
        c.flags["t"] = duration
        c.flags["framerate"] = fps
        return c


    def get_size(self):
        """
        Retrieves the resolution (width and height) of the video file.

        Uses FFprobe to extract the width and height of the first video stream 
        in the video file.

        Returns:
            tuple[int, int]: A tuple containing the width and height of the video.
        """
        data = ffprobe(
            self.filepath,
            (
                "-v",
                "error",
                "-select_streams",
                "v:0",
                "-show_entries",
                "stream=width,height",
            ),
        )["streams"][0]
        return data["width"], data["height"]

    def __repr__(self) -> str:
        return f"<VideoFile filepath={self.filepath}>"

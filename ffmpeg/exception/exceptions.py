class FFmpegException(Exception):
    def __init__(self, msg, return_code) -> None:
        self.msg = msg  # .replace("\n", " ")
        self.return_code = return_code

    def __str__(self) -> str:
        return f"FFmpegException Messge : \n\n{self.msg}"


class FFprobeException(FFmpegException):
    def __init__(self, msg, return_code) -> None:
        self.msg = msg  # .replace("\n", " ")
        self.return_code = return_code

    def __str__(self) -> str:
        return f"FFprobeException Message : \n\n{self.msg}"

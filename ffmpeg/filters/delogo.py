from .base import BaseFilter


class Delogo(BaseFilter):
    def __init__(self, x: int, y: int, w: int, h: int, show: int = 1):
        super().__init__("delogo")
        self.flags = {
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "show": show,
        }

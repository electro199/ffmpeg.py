from typing import Literal
from .base import BaseFilter
from .mixins.enable import TimelineEditingMixin


class Box(BaseFilter, TimelineEditingMixin):
    def __init__(
        self,
        x: float,
        y: float,
        width: float,
        height: float,
        color: str = "red",
        t: int | Literal["fill"] = 5,
        replace: bool = False,
    ):
        super().__init__("drawbox")
        self.flags = {
            "x": x,
            "y": y,
            "w": width,
            "h": height,
            "color": color,
            "t": t,
            "replace": replace,
        }
        # self.flags.update(kwargs)

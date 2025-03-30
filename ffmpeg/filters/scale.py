from enum import IntEnum, StrEnum
from typing import Unpack, TypedDict
from .base import BaseFilter


class EvalMode(StrEnum):
    INIT = "init"
    FRAME = "frame"


class InterlacingMode(IntEnum):
    ENABLED = 1
    DISABLED = 0
    AUTO = -1


class Intent(StrEnum):
    PERCEPTUAL = "perceptual"
    RELATIVE_COLORIMETRIC = "relative_colorimetric"
    ABSOLUTE_COLORIMETRIC = "absolute_colorimetric"
    SATURATION = "saturation"


class ColorMatrix(StrEnum):
    AUTO = "auto"
    BT709 = "bt709"
    FCC = "fcc"
    BT601 = "bt601"
    BT470 = "bt470"
    SMPTE170M = "smpte170m"
    SMPTE240M = "smpte240m"
    BT2020 = "bt2020"


class IORange(StrEnum):
    AUTO = "auto"
    JPEG = "jpeg"
    MPEG = "mpeg"


class IOChromaLocation(StrEnum):
    AUTO = "auto"
    UNKNOWN = "unknown"
    LEFT = "left"
    CENTER = "center"
    TOPLEFT = "topleft"
    TOP = "top"
    BOTTOMLEFT = "bottomleft"
    BOTTOM = "bottom"


class IOPrimaries(StrEnum):
    AUTO = "auto"
    BT709 = "bt709"
    BT470M = "bt470m"
    BT470BG = "bt470bg"
    SMPTE170M = "smpte170m"
    SMPTE240M = "smpte240m"
    FILM = "film"
    BT2020 = "bt2020"
    SMPTE428 = "smpte428"
    SMPTE431 = "smpte431"
    SMPTE432 = "smpte432"
    JEDEC_P22 = "jedec-p22"
    EBU3213 = "ebu3213"


class AspectRatioMode(StrEnum):
    DISABLE = "disable"
    DECREASE = "decrease"
    INCREASE = "increase"


class ScaleFilterOptionsDict(TypedDict, total=False):

    eval: EvalMode
    interl: InterlacingMode
    intent: Intent
    in_color_matrix: ColorMatrix
    out_color_matrix: ColorMatrix
    in_range: IORange
    out_range: IORange

    in_chroma_loc: IOChromaLocation
    out_chroma_loc: IOChromaLocation
    in_primaries: IOPrimaries
    out_primaries: IOPrimaries
    force_original_aspect_ratio: AspectRatioMode
    force_divisible_by: int
    reset_sar: bool


class Scale(BaseFilter):
    def __init__(
        self, width: float, height: float, **kwargs: Unpack[ScaleFilterOptionsDict]
    ):
        super().__init__("scale")
        self.width = width
        self.height = height
        self.flags = {}
        self.flags.update({"width": width, "height": height})
        self.flags.update(kwargs)

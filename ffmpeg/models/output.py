from typing import Iterable, Literal, Optional
from ..inputs import BaseInput, StreamSpecifier

class Map:
    def __init__(
        self,
        node: BaseInput | StreamSpecifier,
        suffix_flags: Optional[dict] = None,
        stream_type: Optional[Literal["a", "v", "s"]] = None,
        **flags,
    ) -> None:
        self.node = node
        self.stream_type = stream_type
        self.suffix_flags = {}
        if suffix_flags:
            self.suffix_flags = {**suffix_flags}
        self.flags = {**flags}


class OutFile:
    def __init__(self, maps: Iterable[Map], path, **kvflags) -> None:
        self.maps, self.path, self.kvflags = maps, path, kvflags

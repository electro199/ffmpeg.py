from typing import Iterable, Optional
from .base import BaseFilter
from ..inputs.streams import StreamSpecifier


class Concat(BaseFilter):
    """
    Represents an overlay filter that combines streams.

    """

    def __init__(self, nodes:list):
        super().__init__("concat")
        self.clips = nodes
        self.parent_nodes = []
        self.flags["n"] = len(self.clips)  + 1 # assuming the first one is from apply fucution
        self.flags["v"] = 1

    def get_outputs(self):
        if self.clips != self.parent_nodes:
            self.parent_nodes.extend(self.clips)

        return (
            StreamSpecifier(self)
            if self.output_count == 1
            else [StreamSpecifier(self, i) for i in range(self.output_count)]
        )
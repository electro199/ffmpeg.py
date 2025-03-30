from typing import Optional
from .base import BaseFilter
from .mixins.enable import TimelineEditingMixin
from ..inputs.streams import StreamSpecifier

class OverlayFilter(BaseFilter, TimelineEditingMixin):
    """
    Represents an overlay filter that combines two video streams.

    """

    def __init__(self, overlay_input: Optional["BaseInput"], x: int, y: int):
        super().__init__("overlay")
        self.overlay_node = overlay_input
        self.flags["x"] = x
        self.flags["y"] = y

        # Expecting two inputs by default (background and overlay)

    def get_outputs(self):
        if self.overlay_node not in self.parent_nodes:
            self.parent_nodes.append(self.overlay_node)

        return (
            StreamSpecifier(self)
            if self.output_count == 1
            else [StreamSpecifier(self, i) for i in range(self.output_count)]
        )
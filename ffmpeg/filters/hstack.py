from .base import BaseFilter
from ..inputs.streams import StreamSpecifier


class HorizontalStack(BaseFilter):
    """
    Represents an hstack filter that combines streams.

    """

    def __init__(self, *nodes, end_on_shortest: bool = False):
        super().__init__("hstack")
        self.clips = nodes
        self.parent_nodes = []
        self.flags["inputs"] = (
            len(self.clips) + 1
        )  # assuming the first one is from apply function
        self.flags["shortest"] = int(end_on_shortest)

    def get_outputs(self):
        if self.clips != self.parent_nodes:
            self.parent_nodes.extend(self.clips)

        return (
            StreamSpecifier(self)
            if self.output_count == 1
            else [StreamSpecifier(self, i) for i in range(self.output_count)]
        )

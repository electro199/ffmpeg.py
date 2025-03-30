from typing import Union
from ..inputs.streams import StreamSpecifier

"""
-i 1.png
-i 2.png
-i 3.png

-f  [1]filter=2=d:s:d[a] ;
    [a]filter=2=d:s:d[b]
    |----Filter-----|

Whole node in command
----
-f  [1]filter=2=d:s:d[a]
    [a]filter=2=d:s:d[b]
    |----Filter-----|

Node in Object form
FilterNode holds :
    parent node reference 
    Filter reference that will be used make filter expression
"""


class BaseFilter:
    """Base class for all FFmpeg filters."""

    def __init__(self, filter_name: str) -> None:

        self.filter_name = filter_name
        self.flags: dict = {}  # all args

        self.parent_nodes: list["BaseInput" | BaseFilter | StreamSpecifier] = []
        self.parent_stream: list[int | str | None] = []

        self.output_count = 1

    def add_input(self, node: Union["BaseInput", "BaseFilter"]):
        self.parent_nodes.append(node)

    def build(self) -> str:
        s = []
        for k, v in self.flags.items():
            s.append(f"{k}={v}")

        return f"{self.filter_name}=" + (":".join(s))

    def get_outputs(self):
        return (
            StreamSpecifier(self)
            if self.output_count == 1
            else [StreamSpecifier(self, i) for i in range(self.output_count)]
        )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}, flags={self.flags}>"  # TODO get better printing scheme

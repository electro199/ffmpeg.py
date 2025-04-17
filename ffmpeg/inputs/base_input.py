from .streams import StreamSpecifier
from abc import ABC, abstractmethod
from ..utils.commons import build_flags

class BaseInput(ABC):
    def __init__(self) -> None:
        self.flags = {}

    @abstractmethod
    def build_input_flags(self) -> list[str]:
        raise NotImplementedError()

    def build(self):
        return build_flags(self.flags)

    def get_outputs(self):
        return StreamSpecifier(self)

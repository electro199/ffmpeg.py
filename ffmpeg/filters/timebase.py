from .base import BaseFilter
from .mixins.enable import TimelineEditingMixin


class SetTimeBase(BaseFilter, TimelineEditingMixin):
    def __init__(self, expression="AVTB"):
        super().__init__("settb")
        self.flags = {"expr": expression}

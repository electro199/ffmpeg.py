from .base import BaseFilter


class SetSampleAspectRatio(BaseFilter):
    def __init__(self, expression="1"):
        super().__init__("setsar")
        self.flags = {"sar": expression}

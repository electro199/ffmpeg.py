from .base import BaseFilter

class Split(BaseFilter):
    def __init__(self, n: int):
        super().__init__("split")
        self.n_streams = n
        self.output_count= n

    def build(self) -> str:
        return f"{self.filter_name}={self.n_streams}"

class VirtualInput:
    def __init__(self, format_flag: str, input_flag: str) -> None:
        self.format_flag = format_flag  # Example: "lavfi"
        self.input_flag = input_flag  # Example: "color=c=red:s=1920x1080"

    def build(self) -> list:
        return ["-f", self.format_flag, "-i", self.input_flag]

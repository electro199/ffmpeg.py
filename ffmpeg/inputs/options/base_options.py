from typing import Optional


class BaseOptions:
    def __init__(self, *args, **kwargs) -> None:
        self.args = []
        self.args.extend(args)
        self.kwargs = kwargs

    def build(self):
        flags = []

        for v in self.args:
            flags.append(f"-{v}")

        for k, v in self.kwargs.items():
            flags.extend((f"-{k}", str(v)))

        return flags

class TimelineEditingMixin:
    flags: dict

    def enable_between(self, start, end):
        self.flags.update({"enable": rf"between(t\,{start}\,{end})"})
        return self

    def enable_after(self, t: float):
        self.flags.update({"enable": rf"gte(t\,{t})"})
        return self

    def enable_before(self, t: float):
        self.flags.update({"enable": rf"lte(t\,{t})"})
        return self

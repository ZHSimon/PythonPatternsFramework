class TGDefaultingDict(dict):
    def __init__(self, default=None, seq=None, **kwargs):
        super().__init__(seq=seq, **kwargs)
        self.default_value = default

    def get(self, key, **kwargs):
        return super().get(key, **kwargs) if super().get(key, **kwargs) else self.default_value

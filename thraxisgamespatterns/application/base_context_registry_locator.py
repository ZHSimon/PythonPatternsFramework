class TGBaseContextRegistryLocator:
    def __init__(self):
        self.registry = ""

    def locate_registry(self, context=None):
        return self.registry


DEFAULT = TGBaseContextRegistryLocator()

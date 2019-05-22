class TGBaseContextRegistryLocator:
    def __init__(self):
        self.registry = ""

    def locate_registry(self, context):
        return self.registry


DEFAULT = TGBaseContextRegistryLocator()

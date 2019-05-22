from abc import ABC, abstractmethod


class TGAbstractPopulatingTransformer(ABC):
    def convert(self, original):
        target = self.create_target()
        self.populate(original, target)
        return target

    @abstractmethod
    def create_target(self):
        pass

    def default_transformation(self):
        return self.create_target()

    @staticmethod
    def match_contents(source, target):
        target.clear()
        target.append(source)

    def populate(self, source, target):
        if source:
            self.populate_contents(source, target)

    @abstractmethod
    def populate_contents(self, source, target):
        pass

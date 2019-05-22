from abc import ABC, abstractmethod


class TGAbstractBaseTransformer(ABC):

    @staticmethod
    def add_non_blank(strings_list=[], new_string=""):
        string = new_string.strip()
        if string:
            strings_list.append(string)

    @abstractmethod
    def convert(self, original):
        pass

    @staticmethod
    def default_transformation():
        return None

    def transform(self, original):
        return self.default_transformation() if not original else self.convert(original)

    def transform_all(self, items_in, items_out=None):
        if items_out:
            items_out.clear()
        if not items_out:
            items_out = []
        for item in items_in:
            items_out.append(self.transform(item))

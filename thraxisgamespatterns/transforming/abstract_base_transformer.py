from abc import ABC, abstractmethod

from thraxisgamespatterns.enumeration.enumerator.basic_enumerator import TGBasicEnumerator


class TGAbstractBaseTransformer(ABC):
    def __init__(self):
        self.enumerator = TGBasicEnumerator()

    def add_non_blank(self, strings_list=[], new_string=""):
        string = new_string.strip()
        if self.ensure_not_null(string):
            strings_list.append(string)

    def any_satisfy(self, items, matcher):
        return self.enumerator.any_satisfy(items, matcher)

    def coalesce(self, primary, alternate):
        return self.enumerator.coalesce(primary, alternate)

    @abstractmethod
    def convert(self, original):
        pass

    @staticmethod
    def default_transformation():
        return None

    def ensure_not_null(self, value):
        return self.coalesce(value, "")

    def first_item(self, items, default_item):
        return self.enumerator.first_item(items, default_item)

    def first_match(self, items, matcher, default_item):
        return self.enumerator.first_match(items, matcher, default_item)

    def select(self, items, matcher):
        return self.enumerator.select(items, matcher)

    def transform(self, original):
        return self.default_transformation() if not original else self.convert(original)

    def transform_all(self, items_in, items_out=None):
        if items_out:
            items_out.clear()
        if not items_out:
            items_out = []
        for item in items_in:
            items_out.append(self.transform(item))

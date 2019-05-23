from abc import abstractmethod

from thraxisgamespatterns.enumeration.enums.abstract_representable import TGAbstractRepresentable
from thraxisgamespatterns.transforming.abstract_base_transformer import TGAbstractBaseTransformer


def create_conversion_map(known_values):
    return_map = {}
    for each in known_values:
        if not isinstance(each, TGAbstractRepresentable):
            raise Exception
        return_map.update({each.get_code(): each})
    return return_map


class TGAbstractRepresentableTransformer(TGAbstractBaseTransformer):
    def __init__(self, known_values=None, conversion_map={}):
        super().__init__()
        self.conversion_map = conversion_map if conversion_map else create_conversion_map(known_values)

    def convert(self, original):
        entry = self.conversion_map.get(original)
        return entry if entry else self.convert_missing(original)

    def convert_missing(self, code):
        normal = code.strip()
        return self.get_unspecified_transformation() if not normal else self.create_unrecognized_value(code)

    @abstractmethod
    def get_unspecified_transformation(self):
        pass

    @abstractmethod
    def create_unrecognized_value(self, code):
        pass

    def default_transformation(self):
        return self.get_unspecified_transformation()

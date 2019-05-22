from thraxisgamespatterns.transforming.abstract_representable_transformer import TGAbstractRepresentableTransformer


def new_instance(known_values, unknown_value, unspecified_value=None):
    return TGBaseRepresentableTransformer(known_values, unknown_value, unspecified_value)


class TGBaseRepresentableTransformer(TGAbstractRepresentableTransformer):
    def __init__(self, known_values, unrecognized_value, unspecified_value=None):
        super().__init__(known_values)
        self.unrecognized_value = unrecognized_value
        self.unspecified_value = unspecified_value if unspecified_value else unrecognized_value

    def create_unrecognized_value(self, code):
        return self.unrecognized_value

    def get_unspecified_transformation(self):
        return self.unspecified_value

from thraxisgamespatterns.enumeration.matcher.abstract_value_matcher import TGAbstractValueMatcher
from thraxisgamespatterns.eventhandling.abstract_reaction import TGAbstractReaction
from thraxisgamespatterns.rules.abstract_applicable import TGAbstractApplicable
from thraxisgamespatterns.transforming.abstract_base_transformer import TGAbstractBaseTransformer


class TGElementMatcher(TGAbstractValueMatcher):
    def get_value_to_match_from(self, element):
        return element.value


class TestElement(TGAbstractApplicable):

    def __init__(self, value="value"):
        self.value = value

    def is_applicable(self, context: str):
        return context == self.value

    def apply_to(self, context: str):
        return context == self.value


class TestElementTransformed(TGAbstractApplicable):
    def __init__(self, value="value"):
        self.transformed_value = value

    def is_applicable(self, context):
        return context

    def apply_to(self, context):
        return context


class TGElementTransformer(TGAbstractBaseTransformer):
    def convert(self, original: TestElement):
        return TestElementTransformed(original.value)


class TGElementReaction(TGAbstractReaction):
    def react_to(self, subject: TestElement):
        subject.value = subject.value.capitalize()

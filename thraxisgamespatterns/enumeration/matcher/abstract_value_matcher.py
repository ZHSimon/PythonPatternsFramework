from abc import abstractmethod

from thraxisgamespatterns.enumeration.matcher.abstract_matcher import TGAbstractMatcher


class TGAbstractValueMatcher(TGAbstractMatcher):
    def __init__(self, values_being_matched):
        if type(values_being_matched) is not list:
            values_being_matched = [values_being_matched]
        self.values_being_matched = values_being_matched

    def is_match(self, element):
        return element is not None and self.values_being_matched.contains(self.get_value_to_match_from(element))

    @abstractmethod
    def get_value_to_match_from(self, element):
        pass

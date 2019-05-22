from abc import abstractmethod

from thraxisgamespatterns.enumeration.matcher.abstract_matcher import TGAbstractMatcher


class TGAbstractValueMatcher(TGAbstractMatcher):
    def __init__(self, values_being_matched):
        if type(values_being_matched) is not list:
            values_being_matched = [values_being_matched]
        self.values_being_matched = values_being_matched

    def is_match(self, element):
        return element and self.get_value_to_match_from(element) in self.values_being_matched

    @abstractmethod
    def get_value_to_match_from(self, element):
        pass

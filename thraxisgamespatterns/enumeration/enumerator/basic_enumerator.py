from thraxisgamespatterns.enumeration.matcher.abstract_matcher import TGAbstractMatcher
from thraxisgamespatterns.eventhandling.abstract_reaction import TGAbstractReaction
from thraxisgamespatterns.patterns.do_nothing_executable import DEFAULT as DO_NOTHING

from thraxisgamespatterns.enumeration.enumerator.abstract_enumerator import TGEnumerator
from thraxisgamespatterns.rules.abstract_applicable import TGAbstractApplicable
from thraxisgamespatterns.transforming.abstract_base_transformer import TGAbstractBaseTransformer


class TGBasicEnumerator(TGEnumerator):
    def any_satisfy(self, items, matcher: TGAbstractMatcher):
        for item in items:
            if matcher.is_match(item):
                return True
        return False

    def coalesce(self, primary, alternate):
        return primary if primary is not None else alternate

    def collect(self, items, matcher: TGAbstractMatcher, transformer: TGAbstractBaseTransformer):
        results = []
        for item in items:
            if matcher.is_match(item):
                results.append(transformer.transform(item))
        return results

    def count(self, items, matcher: TGAbstractMatcher):
        count = 0
        for item in items:
            if matcher.is_match(item):
                count += 1
        return count

    def detect_first_applicable(self, items, situation, default_item: TGAbstractApplicable):
        for item in items:
            if item.is_applicable(situation):
                return item
        return default_item

    def first_item(self, items, default_item):
        return next(iter(items)) if self.is_not_empty(items) else default_item

    def first_match(self, items, matcher: TGAbstractMatcher, default_item):
        for item in items:
            if matcher.is_match(item):
                return item
        return default_item

    @staticmethod
    def is_not_empty(items):
        return items is not None and len(items) > 0

    def none_satisfy(self, items, matcher: TGAbstractMatcher):
        return not self.any_satisfy(items, matcher)

    def react_to_each(self, items, reaction: TGAbstractReaction):
        for item in items:
            reaction.react_to(item)

    def react_to_first_match(self, items, matcher: TGAbstractMatcher,
                             reaction: TGAbstractReaction,
                             on_no_match=DO_NOTHING):
        for item in items:
            if matcher.is_match(item):
                reaction.react_to(item)
                return
        on_no_match.execute()

    def react_to_matches(self, items, matcher: TGAbstractMatcher, reaction: TGAbstractReaction):
        for item in items:
            if matcher.is_match(item):
                reaction.react_to(item)

    def reject(self, items, matcher: TGAbstractMatcher):
        results = []
        for item in items:
            if not matcher.is_match(item):
                results.append(item)
        return results

    def select(self, items, matcher: TGAbstractMatcher):
        results = []
        for item in items:
            if matcher.is_match(item):
                results.append(item)
        return results


DEFAULT = TGBasicEnumerator()

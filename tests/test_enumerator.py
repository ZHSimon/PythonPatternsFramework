from tests.resources_for_tests import TestElement, TGElementMatcher
from thraxisgamespatterns.enumeration.enumerator.basic_enumerator import DEFAULT

list_of_items = [TestElement(), TestElement("value1"), TestElement("value2"), TestElement("value3")]


def test_any_satisfy_true():
    matcher_items = ["value", "value4", "value5", "value"]
    matcher = TGElementMatcher(matcher_items)

    assert DEFAULT.any_satisfy(list_of_items, matcher)


def test_any_satisfy_false():
    matcher_items = ["value7", "value4", "value5", "value6"]
    matcher = TGElementMatcher(matcher_items)

    assert not DEFAULT.any_satisfy(list_of_items, matcher)


def test_coalesce_primary():
    actual = DEFAULT.coalesce("primary", "secondary")
    expected = "primary"

    assert actual == expected


def test_coalesce_secondary():
    actual = DEFAULT.coalesce("", "secondary")
    expected = "secondary"

    assert actual == expected


def test_count():
    matcher_items = ["value1", "value4", "value3", "value5"]
    matcher = TGElementMatcher(matcher_items)
    expected = 2
    actual = DEFAULT.count(list_of_items, matcher)

    assert actual == expected


def test_detect_first_applicable():
    situation = "value1"
    default_item = list_of_items[0]
    expected = list_of_items[1]

    actual = DEFAULT.detect_first_applicable(list_of_items, situation, default_item)

    assert actual == expected


def test_detect_first_applicable_default():
    situation = "NOPE"
    default_item = TestElement()
    expected = default_item

    actual = DEFAULT.detect_first_applicable(list_of_items, situation, default_item)

    assert actual == expected


def test_first_match():
    matcher_items = ["value1", "value4", "value3", "value5"]
    matcher = TGElementMatcher(matcher_items)
    default_item = list_of_items[0]
    expected = list_of_items[1]

    actual = DEFAULT.first_match(list_of_items, matcher, default_item)

    assert actual == expected


def test_first_match_default():
    matcher_items = ["value6", "value4", "value11", "value5"]
    matcher = TGElementMatcher(matcher_items)
    default_item = TestElement()
    expected = default_item

    actual = DEFAULT.first_match(list_of_items, matcher, default_item)

    assert actual == expected


def test_is_not_empty():
    assert DEFAULT.is_not_empty(list_of_items)


def test_none_satisfy_true():
    matcher_items = [TestElement("value6"), TestElement("value4"), TestElement("value5"), TestElement("value7")]
    matcher = TGElementMatcher(matcher_items)

    assert DEFAULT.none_satisfy(list_of_items, matcher)


def test_none_satisfy_false():
    matcher_items = ["value14", "value4", "value9", "value5"]
    matcher = TGElementMatcher(matcher_items)

    assert DEFAULT.none_satisfy(list_of_items, matcher)

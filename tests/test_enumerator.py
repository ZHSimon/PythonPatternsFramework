from thraxisgamespatterns.enumeration.enumerator.basic_enumerator import TGBasicEnumerator, DEFAULT
from tests.resources_for_tests import TestElement, TGElementMatcher, TGElementTransformer

list_of_items = [TestElement(), TestElement("value1"), TestElement("value2"), TestElement("value3")]


def test_create():
    actual = TGBasicEnumerator()
    expected = DEFAULT

    assert actual == expected


def test_any_satisfy_true():
    matcher_items = [TestElement(), TestElement("value4"), TestElement("value5"), TestElement()]
    matcher = TGElementMatcher(matcher_items)

    assert DEFAULT.any_satisfy(list_of_items, matcher)


def test_any_satisfy_false():
    matcher_items = [TestElement("value6"), TestElement("value4"), TestElement("value5"), TestElement("value7")]
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


def test_collect():
    matcher_items = [TestElement("value4"), TestElement("value3"), TestElement("value2"), TestElement("value1")]
    matcher = TGElementMatcher(matcher_items)
    transformer = TGElementTransformer()

    expected = [TestElement(), TestElement("value1"), TestElement("value2"), TestElement("value3"),
                TestElement("value3"), TestElement("value2"), TestElement("value1")]
    actual = DEFAULT.collect(list_of_items, matcher, transformer)

    assert actual == expected


def test_count():
    matcher_items = [TestElement("value4"), TestElement("value3"), TestElement("value2"), TestElement("value1")]
    matcher = TGElementMatcher(matcher_items)
    expected = 1
    actual = DEFAULT.count(list_of_items, matcher)

    assert actual == expected


def test_detect_first_applicable():
    situation = "value1"
    default_item = TestElement()
    expected = TestElement("value1")

    actual = DEFAULT.detect_first_applicable(list_of_items, situation, default_item)

    assert actual == expected


def test_detect_first_applicable_default():
    situation = "NOPE"
    default_item = TestElement()
    expected = default_item

    actual = DEFAULT.detect_first_applicable(list_of_items, situation, default_item)

    assert actual == expected


def test_first_match():
    situation = "value1"
    default_item = TestElement()
    expected = TestElement("value1")

    actual = DEFAULT.first_match(list_of_items, situation, default_item)

    assert actual == expected


def test_first_match_default():
    situation = "NOPE"
    default_item = TestElement()
    expected = default_item

    actual = DEFAULT.first_match(list_of_items, situation, default_item)

    assert actual == expected


def test_is_not_empty():
    assert DEFAULT.is_not_empty(list_of_items)


def test_none_satisfy_true():
    matcher_items = [TestElement("value6"), TestElement("value4"), TestElement("value5"), TestElement("value7")]
    matcher = TGElementMatcher(matcher_items)

    assert DEFAULT.none_satisfy(list_of_items, matcher)


def test_none_satisfy_false():
    matcher_items = [TestElement(), TestElement("value4"), TestElement("value5"), TestElement()]
    matcher = TGElementMatcher(matcher_items)

    assert DEFAULT.none_satisfy(list_of_items, matcher)




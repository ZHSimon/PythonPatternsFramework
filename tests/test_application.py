import logging

from thraxisgamespatterns.application.abstract_registry import TGAbstractRegistry
from thraxisgamespatterns.application.base_context_registry_locator import DEFAULT
from thraxisgamespatterns.application.handler_map_factory import TGHandlerMapFactory
from thraxisgamespatterns.eventhandling.event_distributor import TGEventDistributor
from thraxisgamespatterns.rules.logging_rule_engine import TGLoggingRuleEngine


def test_create_registry():
    registry = TGAbstractRegistry()
    actual_rule_engine = isinstance(registry.rule_engine, TGLoggingRuleEngine)
    actual_logger = registry.logger == logging.getLogger()
    actual_event_distributor = registry.event_distributor == TGEventDistributor(logging.getLogger())
    actual_handler_map_factory = registry.handler_map_factory == {}
    print(actual_event_distributor, actual_handler_map_factory, actual_logger, actual_rule_engine)
    assert actual_event_distributor and actual_handler_map_factory and actual_logger and actual_rule_engine


def test_base_context_get_registry():
    actual = DEFAULT.locate_registry(None)
    expected = ""

    assert actual == expected


def test_handler_map_factory_create():
    actual = TGHandlerMapFactory().create()
    expected = {}

    assert actual == expected

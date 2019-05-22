import logging

from thraxisgamespatterns.application.abstract_registry import TGAbstractRegistry
from thraxisgamespatterns.application.base_context_registry_locator import TGBaseContextRegistryLocator, DEFAULT
from thraxisgamespatterns.application.handler_map_factory import TGHandlerMapFactory
from thraxisgamespatterns.eventhandling.event_distributor import TGEventDistributor
from thraxisgamespatterns.factories.logging_rule_engine_factory import TGLoggingRuleEngineFactory


def test_create_registry():
    registry = TGAbstractRegistry()
    actual_rule_engine = registry.rule_engine == TGLoggingRuleEngineFactory().create()
    actual_logger = registry.logger == logging.getLogger()
    actual_event_distributor = registry.event_distributor == TGEventDistributor(logging.getLogger())
    actual_handler_map_factory = registry.handler_map_factory == TGHandlerMapFactory().create()

    assert actual_event_distributor and actual_handler_map_factory and actual_logger and actual_rule_engine


def test_base_context_create():
    actual = TGBaseContextRegistryLocator()
    expected = DEFAULT

    assert actual == expected


def test_base_context_get_registry():
    actual = DEFAULT.locate_registry(None)
    expected = ""

    assert actual == expected


def test_handler_map_factory_create():
    actual = TGHandlerMapFactory().create()
    expected = {}

    assert actual == expected

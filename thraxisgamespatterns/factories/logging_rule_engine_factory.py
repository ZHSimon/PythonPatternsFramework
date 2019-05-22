import logging

from thraxisgamespatterns.factories.abstract_factory import TGAbstractFactory
from thraxisgamespatterns.rules.logging_rule_engine import TGLoggingRuleEngine


class TGLoggingRuleEngineFactory(TGAbstractFactory):

    def create(self, options=None):
        return TGLoggingRuleEngine(logging.getLogger())

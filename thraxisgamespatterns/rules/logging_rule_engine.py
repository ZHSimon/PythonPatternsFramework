from thraxisgamespatterns.rules.rule_engine import TGBaseRuleEngine


class TGLoggingRuleEngine(TGBaseRuleEngine):
    def __init__(self, logger, formatting="Applying Rule: {}"):
        self.logger = logger
        self.formatting = formatting

    def apply_rule(self, rule, context):
        self.log_rule_applied(rule)
        super().apply_rule(rule, context)

    def log_rule_applied(self, rule):
        self.logger.info(self.formatting, rule)

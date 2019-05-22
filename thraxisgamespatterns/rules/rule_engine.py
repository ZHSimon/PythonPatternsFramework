class TGBaseRuleEngine:

    def apply_all(self, rules, context=None):
        for rule in rules:
            self.consider_applying(context, rule)

    def apply_first(self, rules, context=None):
        for rule in rules:
            if rule.is_applicable(context):
                self.apply_rule(rule, context)
                return

    @staticmethod
    def apply_rule(rule, context):
        rule.apply_to(context)

    def consider_applying(self, context, rule):
        if rule.is_applicable(context):
            self.apply_rule(rule, context)


DEFAULT = TGBaseRuleEngine()

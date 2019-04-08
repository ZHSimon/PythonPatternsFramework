# package com.games.thraxis.framework.rules;
#
# /##
#  # Created by Zack on 10/2/2017.
#  #/
#
# public abstract class TGDoNothingStatefulRule extends TGBaseStatefulRule {
#
# 	@Override
# 	public void apply() {
# 		//DO NOTHING
# 	}
#
# 	@Override
# 	public abstract String toString();
# }
from rules.abstract_stateful_rule import TGAbstractStatefulRule


class TGDoNothingStatefulRule(TGAbstractStatefulRule):
    def apply(self):
        pass  # Do nothing.

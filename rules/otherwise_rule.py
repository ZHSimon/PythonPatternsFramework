# package com.games.thraxis.framework.rules;
#
# /##
#  # Created by Zack on 10/2/2017.
#  #/
#
# public abstract class TGOtherwiseRule<C> extends TGBaseRule<C> {
#
# 	@Override
# 	public boolean isApplicable(C context) {
# 		return true;
# 	}
#
#
# 	@Override
# 	public abstract String toString();
# }
#
from rules.abstract_rule import TGAbstractRule
from abc import ABC


class TGAbstractOtherwiseRule(ABC, TGAbstractRule):
    @staticmethod
    def is_applicable(context=None):
        return True

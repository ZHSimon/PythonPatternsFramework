# package com.games.thraxis.framework.rules;
#
# /##
#  # Provides common behaviors for stateless condition and action pairs that can apply themselves when appropriate
#  #
#  # Concrete implementations should be stateless and safe to use on multiple threads
#  #/
#
# public abstract class TGBaseRule<C> implements TGRule<C> {
#
# 	@Override
# 	public void considerApplying(C context) {
# 		if (isApplicable(context)) {
# 			applyTo(context);
# 		}
# 	}
# }

from rules.abstract_applicable import TGAbstractApplicable
from abc import ABC


class TGAbstractRule(ABC, TGAbstractApplicable):
    def consider_applying(self, context):
        if self.is_applicable(context):
            self.apply_to(context)

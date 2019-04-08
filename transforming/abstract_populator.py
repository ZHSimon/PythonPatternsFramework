# package com.games.thraxis.framework.transforming;
#
# /##
#  # Created by Zack on 9/25/2017.
#  #/
#
# public interface TGPopulator<S, T> {
# 	void populate(S source, T target);
#
# }
from abc import ABC, abstractmethod


class TGAbstractPopulator(ABC):
    @abstractmethod
    def populate(self, source, target):
        pass

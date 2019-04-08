# package com.games.thraxis.framework.factories;
#
# /##
#  # Created by Zack on 10/2/2017.
#  #/
#
# public interface TGCustomFactory<P, O> {
# 	P create(O options);
#
# }

from factories.abstract_factory import TGAbstractFactory
from abc import ABC, abstractmethod


class TGAbstractCustomFactory(ABC, TGAbstractFactory):

    @abstractmethod
    def create(self, options):
        pass

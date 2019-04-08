# package com.games.thraxis.framework.enumeration.enums;
#
# /##
#  # Created by Zack on 9/21/2017.
#  #/
#
# public interface TGVisitor {
#
# 	Void NOTHING = null;
#
# }
from abc import ABC, abstractmethod


class TGAbstractVisitor(ABC):
    def __init__(self):
        self.NOTHING = None

    @abstractmethod
    def visit_any(self):
        pass

# package com.games.thraxis.framework.sorting;
#
# import java.util.List;
#
# /##
#  # Created by Zack on 10/19/2017.
#  #/
#
# public interface TGSorter<C> {
# 	List<C> sort();
# }
from abc import ABC, abstractmethod


class TGAbstractSorter(ABC):
    @abstractmethod
    def sort(self):
        pass

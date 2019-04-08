# package com.games.thraxis.framework.transforming;
#
# import java.util.Collection;
# import java.util.List;
#
# /##
#  # Created by Zack on 9/24/2017.
#  #/
#
# public interface TGTransformer<O, T> {
#
# 	T transform(O original);
#
# 	void transformAll(Collection<O> inItems, Collection<T> outItems);
#
# 	void transformAll(O[] inItems, Collection<T> outItems);
#
# 	List<T> transformAll(Collection<O> inItems);
# }
from abc import ABC, abstractmethod


class TGAbstractTransformer(ABC):
    @abstractmethod
    def transform(self, original):
        pass

    @abstractmethod
    def transform_all(self, items_in, items_out=None):
        pass

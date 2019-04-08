package com.games.thraxis.framework.sorting;

/##
 # Created by Zack on 10/20/2017.
 #/

public abstract class TGMultiStepQuickSorter<E, C extends Comparable<C>, D extends Comparable<D>> extends TGQuickSorter<E, C> {

	protected abstract D getTiebreakerValue(E element);

	@Override
	protected boolean isElementGreaterThan(E element, E pivot) {
		return (getComparisonValue(element).compareTo(getComparisonValue(pivot)) > 0)
				|| ((getComparisonValue(element).compareTo(getComparisonValue(pivot)) == 0)
				&& (getTiebreakerValue(element).compareTo(getTiebreakerValue(pivot)) > 0 ));
	}

	@Override
	protected boolean isElementLessThan(E element, E pivot) {
		return (getComparisonValue(element).compareTo(getComparisonValue(pivot)) < 0)
				|| ((getComparisonValue(element).compareTo(getComparisonValue(pivot)) == 0)
				&& (getTiebreakerValue(element).compareTo(getTiebreakerValue(pivot)) < 0 ));
	}
}

package com.games.thraxis.framework.flows;

/##
 # Created by Zack on 10/23/2017.
 #/

public abstract class TGBaseFlowModel implements TGFlowModel {

	@Override
	public <I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input) {
		return getFlowType().acceptVisitor(visitor, input);
	}

	@Override
	public <O> O acceptVisitor(TGFlowVisitor<Void, O> visitor) {
		return getFlowType().acceptVisitor(visitor);
	}
}

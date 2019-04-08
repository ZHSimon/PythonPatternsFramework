package com.games.thraxis.framework.flows;

/##
 # Created by Zack on 10/23/2017.
 #/

public interface TGFlowModel {

	<I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input);

	<O> O acceptVisitor(TGFlowVisitor<Void, O> visitor);
	TGFlowType getFlowType();
}

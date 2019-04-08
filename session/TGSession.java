package com.games.thraxis.framework.session;

import com.games.thraxis.core.cards.MtgCardFlow;
import com.games.thraxis.framework.flows.TGFlowType;
import com.games.thraxis.framework.flows.TGFlowVisitor;

/##
 # Created by Zack on 10/23/2017.
 #/

public interface TGSession extends TGConstants {

	<O> O acceptVisitor(TGFlowVisitor<Void, O> visitor);

	TGFlowType getActiveFlowType();

	long computeSecondsSinceLastKeptAlive();

	MtgCardFlow getCardFlow();

	void updateKeptAliveAtTimestamp();

}

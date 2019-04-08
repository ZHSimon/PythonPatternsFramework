package com.games.thraxis.framework.session;

import com.games.thraxis.core.cards.MtgCardFlow;
import com.games.thraxis.framework.flows.TGFlowType;
import com.games.thraxis.framework.flows.TGFlowVisitor;

/##
 # Created by Zack on 10/23/2017.
 #/

public class TGBasicSession implements TGSession {

	private TGFlowType activeFlowType = TGFlowType.CARD;
	private final MtgCardFlow cardFlow = new MtgCardFlow();

	private long keptAliveAtTimestamp = 0L;

	@Override
	public <O> O acceptVisitor(TGFlowVisitor<Void, O> visitor) {
		return getActiveFlowType().acceptVisitor(visitor);
	}

	@Override
	public TGFlowType getActiveFlowType() {
		return activeFlowType;
	}

	@Override
	public long computeSecondsSinceLastKeptAlive() {
		return (System.currentTimeMillis() - keptAliveAtTimestamp) / 1000L;
	}

	@Override
	public MtgCardFlow getCardFlow() {
		return cardFlow;
	}

	@Override
	public void updateKeptAliveAtTimestamp() {
		keptAliveAtTimestamp = System.currentTimeMillis();
	}
}

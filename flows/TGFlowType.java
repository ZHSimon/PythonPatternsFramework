package com.games.thraxis.framework.flows;

import com.games.thraxis.framework.enumeration.enums.TGVisitor;

/##
 # Created by Zack on 10/23/2017.
 #/

public enum TGFlowType {
	CARD {
		@Override
		public <I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input) {
			return visitor.visitCardFlow(input);
		}
	},
	COLLECTION {
		@Override
		public <I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input) {
			return visitor.visitCollectionFlow(input);
		}
	},
	DECK {
		@Override
		public <I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input) {
			return visitor.visitDeckFlow(input);
		}
	},
	GAME {
		@Override
		public <I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input) {
			return visitor.visitGameFlow(input);
		}
	};


	public abstract <I, O> O acceptVisitor(TGFlowVisitor<I, O> visitor, I input);
	public <O> O acceptVisitor(TGFlowVisitor<Void, O> visitor) {
		return acceptVisitor(visitor, TGVisitor.NOTHING);
	}
}

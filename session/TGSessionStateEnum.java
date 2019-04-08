package com.games.thraxis.framework.session;

import com.games.thraxis.framework.enumeration.enums.TGVisitor;

/##
 # Created by Zack on 10/23/2017.
 #/

public enum TGSessionStateEnum implements TGSessionState {
	NOT_AUTHENTICATED {
		@Override
		public <I, O> O acceptVisitor(TGSessionStateVisitor<I, O> visitor, I input) {
			return visitor.visitNotAuthenticated(input);
		}

	}, AUTHENTICATED {
		@Override
		public <I, O> O acceptVisitor(TGSessionStateVisitor<I, O> visitor, I input) {
			return visitor.visitAuthenticated(input);
		}

		@Override
		public boolean isAuthenticated() {
			return true;
		}
	};

	public interface TGSessionStateVisitor<I, O> extends TGVisitor {

		O visitAuthenticated(I input);

		O visitNotAuthenticated(I input);
	}

	@Override
	public abstract <I, O> O acceptVisitor(TGSessionStateVisitor<I, O> visitor, I input);

	@Override
	public <O> O acceptVisitor(TGSessionStateVisitor<Void, O> visitor) {
		return acceptVisitor(visitor, null);
	}

	@Override
	public boolean isAuthenticated() {
		return false;
	}
}

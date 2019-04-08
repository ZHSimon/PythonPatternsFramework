package com.games.thraxis.framework.session;

import com.games.thraxis.framework.session.TGSessionStateEnum.TGSessionStateVisitor;

/##
 # Created by Zack on 10/24/2017.
 #/

public interface TGSessionState {

	<I, O> O acceptVisitor(TGSessionStateVisitor<I, O> visitor, I input);

	<O> O acceptVisitor(TGSessionStateVisitor<Void, O> visitor);

	boolean isAuthenticated();
}

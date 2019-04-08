package com.games.thraxis.framework.logging;

import com.games.thraxis.framework.factories.TGFactory;

/##
 # Created by Zack on 10/2/2017.
 #/

public class TGLoggingFactory implements TGFactory<TGLogger> {

	@Override
	public TGLogger create() {
		return new TGBasicLogger();
	}
}

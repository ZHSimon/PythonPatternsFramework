package com.games.thraxis.framework.flows;

import com.games.thraxis.framework.enumeration.enums.TGVisitor;

/##
 # Created by Zack on 10/23/2017.
 #/

public interface TGFlowVisitor<I, O> extends TGVisitor {

	O visitCardFlow(I input);

	O visitCollectionFlow(I input);

	O visitDeckFlow(I input);

	O visitGameFlow(I input);

}

package com.games.thraxis.framework.lifecycle;

import android.app.Activity;
import android.content.Intent;

/##
 # Created by Zack on 9/26/2017.
 #/

public class TGSimpleAppRestarter implements TGAppRestarter {

	private final Class<? extends Activity> mainActivityClass;

	public TGSimpleAppRestarter(Class<? extends Activity> mainActivityClass) {
		this.mainActivityClass = mainActivityClass;
	}

	@Override
	public void restartAp(Activity currentActivity) {
		currentActivity.startActivity(new Intent(currentActivity, mainActivityClass));
	}
}

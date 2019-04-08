package com.games.thraxis.framework.session.controller;

import android.app.Activity;
import android.content.Context;
import android.net.Uri;
import android.support.annotation.NonNull;

import com.games.thraxis.framework.assertions.TGWatchDog;
import com.games.thraxis.framework.eventHandling.TGPublisher;
import com.games.thraxis.framework.flows.TGFlowType;
import com.games.thraxis.framework.rules.TGRuleEngine;
import com.games.thraxis.framework.session.TGSession;

/##
 # Created by Zack on 10/23/2017.
 #/

public interface TGSessionController {
	TGFlowType getActiveFlowType();
	TGSession getSession();
	TGPublisher<String, Object> getPublisher();
	TGRuleEngine getRuleEngine();
	TGWatchDog getWatchdog();
	boolean isInSession();
	void start(Context context, Class <? extends Activity> activity);
	void startAction(Context context, String action);
	void startAction(Context context, String action, Uri uri);
	void startSessionlessAction(Context context, String action);
	void startSession();
	Class<?> getHandlerForAction(@NonNull String action);
}

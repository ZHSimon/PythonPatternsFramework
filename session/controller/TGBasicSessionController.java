package com.games.thraxis.framework.session.controller;

import java.util.Map;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.net.Uri;
import android.support.annotation.NonNull;

import com.games.thraxis.framework.application.TGRegistry;
import com.games.thraxis.framework.assertions.TGWatchDog;
import com.games.thraxis.framework.eventHandling.TGPublisher;
import com.games.thraxis.framework.flows.TGFlowType;
import com.games.thraxis.framework.rules.TGLoggingRuleEngine;
import com.games.thraxis.framework.rules.TGRuleEngine;
import com.games.thraxis.framework.session.TGBasicSession;
import com.games.thraxis.framework.session.TGSession;
import com.games.thraxis.framework.session.TGSessionState;
import com.games.thraxis.framework.session.TGSessionStateEnum;
import com.games.thraxis.framework.session.TGSessionStateEnum.TGSessionStateVisitor;

import static com.games.thraxis.framework.application.TGApplicationConstants.ACTION_LOGIN;

/##
 # Created by Zack on 10/23/2017.
 #/

public class TGBasicSessionController implements TGSessionController {

	private final Map<String, Class<?>> handlersByAction;
	private final TGPublisher<String, Object> publisher;
	private final TGRuleEngine ruleEngine;
	private final TGSession session;
	private TGSessionState sessionState = TGSessionStateEnum.NOT_AUTHENTICATED;
	private final TGWatchDog watchdog;

	public TGBasicSessionController(TGRegistry registry, TGPublisher<String, Object> publisher) {
		this.publisher = publisher;
		this.ruleEngine = new TGLoggingRuleEngine(registry.getLogger());
		this.watchdog = registry.getWatchdog();
		this.session = new TGBasicSession();
		handlersByAction = registry.getHandlersByAction();
	}

	@Override
	public TGFlowType getActiveFlowType() {
		return getSession().getActiveFlowType();
	}

	@NonNull
	@Override
	public Class<?> getHandlerForAction(@NonNull String action) {
		Class<?> handler = handlersByAction.get(action);
		watchdog.assertNotNull(handler, "No handler for action.");
		return handler;
	}

	@Override
	public TGPublisher<String, Object> getPublisher() {
		return publisher;
	}

	@Override
	public TGRuleEngine getRuleEngine() {
		return ruleEngine;
	}

	@Override
	public TGSession getSession() {
		return session;
	}

	@Override
	public TGWatchDog getWatchdog() {
		return watchdog;
	}

	@Override
	public boolean isInSession() {
		return sessionState.isAuthenticated();
	}

	@Override
	public void start(Context context, Class<? extends Activity> activity) {
		start(activity.getSimpleName(), null, context, activity);
	}

	protected void start(final String action, final Uri uri, final Context context, final Class<?> handlerType) {
		sessionState.acceptVisitor(new TGSessionStateVisitor<Void, Void>() {
			protected Void proceedDirectly() {
				Intent nextIntent = new Intent(action, uri, context, handlerType);
				context.startActivity(nextIntent);
				return NOTHING;
			}

			protected Void proceedThrough(String immediateAction) {
				Class<?> immediateHandler = handlersByAction.get(immediateAction);
				context.startActivity(new Intent(action, uri, context, immediateHandler));
				return NOTHING;
			}

			@Override
			public Void visitAuthenticated(Void input) {
				return proceedDirectly();
			}

			@Override
			public Void visitNotAuthenticated(Void input) {
				return proceedThrough(ACTION_LOGIN);
			}
		});
	}

	@Override
	public void startAction(Context context, String action) {
		startAction(context, action, null);
	}

	@Override
	public void startAction(Context context, String action, Uri uri) {
		Class<?> handler = getHandlerForAction(action);
		start(action, uri, context, handler);
	}

	@Override
	public void startSession() {

	}

	@Override
	public void startSessionlessAction(Context context, String action) {
		Class<?> handler = getHandlerForAction(action);
		Intent intent = new Intent(context, handler);
		context.startActivity(intent);

	}
}

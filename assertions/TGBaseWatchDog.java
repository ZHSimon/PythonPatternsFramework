package com.games.thraxis.framework.assertions;

import android.os.Looper;

/##
 # Created by Zack on 9/26/2017.
 #/

public class TGBaseWatchDog implements TGWatchDog {

	public final static TGBaseWatchDog DEFAULT = new TGBaseWatchDog();

	protected static Thread getUserInterfaceThread() {
		return Looper.getMainLooper().getThread();
	}

	@Override
	public void assertBackgroundThread() {
		assertBackgroundThread(null);
	}

	@Override
	public void assertBackgroundThread(String detailMessage) {
		assertTrue(!isRunningInUIThread(), detailMessage);
	}

	@Override
	public void assertFalse(boolean condition, String detailMessage) {
		assertTrue(!condition, detailMessage);
	}

	@Override
	public void assertNotNull(Object value) {
		assertNotNull(value, null);
	}

	@Override
	public void assertNotNull(Object value, String detailMessage) {
		assertTrue(value != null, detailMessage);
	}

	@Override
	public void assertTrue(boolean condition, String detailMessage) {
		if (!condition) {
			throw new IllegalStateException(detailMessage);
		}
	}

	@Override
	public void assertUiThread() {
		assertUiThread(null);
	}

	@Override
	public void assertUiThread(String detailMessage) {
		assertTrue(isRunningInUIThread(), detailMessage);
	}

	protected boolean isRunningInUIThread() {
		return Thread.currentThread() == getUserInterfaceThread();
	}
}

package com.games.thraxis.framework.assertions;

/##
 # Created by Zack on 9/26/2017.
 #/

public interface TGWatchDog {

	void assertBackgroundThread();
	void assertBackgroundThread(String detailMessage);
	void assertFalse(boolean condition, String detailMessage);
	void assertNotNull(Object value);
	void assertNotNull(Object value, String detailMessage);
	void assertTrue(boolean condition, String detailMessage);
	void assertUiThread();
	void assertUiThread(String detailMessage);
}

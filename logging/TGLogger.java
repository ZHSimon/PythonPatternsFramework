package com.games.thraxis.framework.logging;

import android.util.Log;

/##
 # Created by Zack on 10/2/2017.
 #/

public interface TGLogger {

	int ASSERT = Log.ASSERT;
	int DEBUG = Log.DEBUG;
	int ERROR = Log.ERROR;
	int INFO = Log.INFO;
	int VERBOSE = Log.VERBOSE;
	int WARN = Log.WARN;

	int debug(Class<?> originatingType, String message);

	int debug(Class<?> originatingType, String format, Object... arguments);

	int debug(Class<?> originatingType, Throwable throwable);

	int debug(String tag, String message);

	int debug(String tag, String message, Throwable throwable);

	int error(Class<?> originatingType, String message);

	int error(Class<?> originatingType, String format, Object... arguments);

	int error(Class<?> originatingType, String message, Throwable throwable);

	int error(Class<?> originatingType, Throwable throwable);

	int error(Class<?> originatingType, Throwable throwable, String message);

	int error(Class<?> originatingType, Throwable throwable, String format, Object... arguments);

	int error(String tag, String message);

	int error(String tag, String message, Throwable throwable);

	String getStackTraceString(Throwable throwable);

	int info(Class<?> originatingType, String message);

	int info(Class<?> originatingType, String format, Object... arguments);

	int info(String tag, String message);

	int info(String tag, String message, Throwable throwable);

	boolean isLoggable(String tag, int level);

	int println(int priority, String tag, String message);

	int verbose(Class<?> originatingType, String message);

	int verbose(Class<?> originatingType, String format, Object... arguments);

	int verbose(String tag, String message);

	int verbose(String tag, String message, Throwable throwable);

	int warn(Class<?> originatingType, String message);

	int warn(Class<?> originatingType, String format, Object... arguments);

	int warn(Class<?> originatingType, String message, Throwable thowable);

	int warn(String tag, String message);

	int warn(String tag, String message, Throwable throwable);

	int warn(String tag, Throwable throwable);
}

package com.games.thraxis.framework.logging;

import android.util.Log;

/##
 # Created by Zack on 10/2/2017.
 #/

public class TGBasicLogger implements TGLogger {

	@Override
	public int debug(Class<?> originatingType, String message) {
		return println(DEBUG, originatingType, message);
	}

	@Override
	public int debug(Class<?> originatingType, String format, Object... arguments) {
		return println(DEBUG, originatingType, format, arguments);
	}

	@Override
	public int debug(Class<?> originatingType, Throwable throwable) {
		return debug(originatingType, "", throwable);
	}

	@Override
	public int debug(String tag, String message) {
		return Log.d(tag, message);
	}

	@Override
	public int debug(String tag, String message, Throwable throwable) {
		return Log.d(tag, message, throwable);
	}

	@Override
	public int error(Class<?> originatingType, String message) {
		return println(ERROR, originatingType, message);
	}

	@Override
	public int error(Class<?> originatingType, String format, Object... arguments) {
		return println(ERROR, originatingType, format, arguments);
	}

	@Override
	public int error(Class<?> originatingType, String message, Throwable throwable) {
		return println(ERROR, originatingType, message, throwable);
	}

	@Override
	public int error(Class<?> originatingType, Throwable throwable) {
		return error(originatingType, "", throwable);
	}

	@Override
	public int error(Class<?> originatingType, Throwable throwable, String message) {
		return println(ERROR, originatingType, throwable, message);
	}

	@Override
	public int error(Class<?> originatingType, Throwable throwable, String format, Object... arguments) {
		return println(ERROR, originatingType, throwable, format, arguments);
	}

	@Override
	public int error(String tag, String message) {
		return Log.e(tag, message);
	}

	@Override
	public int error(String tag, String message, Throwable throwable) {
		return Log.e(tag, message, throwable);
	}

	@Override
	public String getStackTraceString(Throwable throwable) {
		return Log.getStackTraceString(throwable);
	}

	@Override
	public int info(Class<?> originatingType, String message) {
		return println(INFO, originatingType, message);
	}

	@Override
	public int info(Class<?> originatingType, String format, Object... arguments) {
		return println(INFO, originatingType, format, arguments);
	}

	@Override
	public int info(String tag, String message) {
		return Log.i(tag, message);
	}

	@Override
	public int info(String tag, String message, Throwable throwable) {
		return Log.i(tag, message, throwable);
	}

	@Override
	public boolean isLoggable(String tag, int level) {
		return Log.isLoggable(tag, level);
	}

	protected int println(int priority, Class<?> originatingType, String message) {
		String tag = originatingType.getSimpleName();
		return Log.println(priority, tag, message);
	}

	protected int println(int priority, Class<?> originatingType, String format, Object... arguments) {
		String tag = originatingType.getSimpleName();
		String message = String.format(format, arguments);
		return Log.println(priority, tag, message);
	}

	protected int println(int priority, Class<?> originatingType, String message, Throwable throwable) {
		String tag = originatingType.getSimpleName();
		return println(priority, tag, message + '\n' + getStackTraceString(throwable));
	}

	protected int println(int priority, Class<?> originatingType, Throwable throwable, String format,
			Object... arguments) {
		String tag = originatingType.getSimpleName();
		String message = String.format(format, arguments);
		return Log.println(priority, tag, message + '\n' + getStackTraceString(throwable));
	}

	@Override
	public int println(int priority, String tag, String message) {
		return Log.println(priority, tag, message);
	}

	@Override
	public int verbose(Class<?> originatingType, String message) {
		return println(VERBOSE, originatingType, message);
	}

	@Override
	public int verbose(Class<?> originatingType, String format, Object... arguments) {
		return println(VERBOSE, originatingType, format, arguments);
	}

	@Override
	public int verbose(String tag, String message) {
		return Log.v(tag, message);
	}

	@Override
	public int verbose(String tag, String message, Throwable throwable) {
		return Log.v(tag, message, throwable);
	}

	@Override
	public int warn(Class<?> originatingType, String message) {
		return println(WARN, originatingType, message);
	}

	@Override
	public int warn(Class<?> originatingType, String format, Object... arguments) {
		return println(WARN, originatingType, format, arguments);
	}

	@Override
	public int warn(Class<?> originatingType, String message, Throwable throwable) {
		return println(WARN, originatingType, message, throwable);
	}

	@Override
	public int warn(String tag, String message) {
		return Log.w(tag, message);
	}

	@Override
	public int warn(String tag, String message, Throwable throwable) {
		return Log.w(tag, message, throwable);
	}

	@Override
	public int warn(String tag, Throwable throwable) {
		return Log.w(tag, throwable);
	}
}

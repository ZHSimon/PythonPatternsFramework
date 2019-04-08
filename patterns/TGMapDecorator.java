package com.games.thraxis.framework.patterns;

import java.util.Collection;
import java.util.Map;
import java.util.Set;

import android.support.annotation.NonNull;

/##
 # Created by Zack on 9/26/2017.
 #/

public class TGMapDecorator<K, V> implements Map<K, V> {

	private final Map<K, V> map;

	public TGMapDecorator(Map<K, V> map) {
		this.map = map;
	}

	@Override
	public void clear() {
		map.clear();
	}

	@Override
	public boolean containsKey(Object key) {
		return map.containsKey(key);
	}

	@Override
	public boolean containsValue(Object value) {
		return map.containsValue(value);
	}

	@NonNull
	@Override
	public Set<Entry<K, V>> entrySet() {
		return map.entrySet();
	}

	@Override
	public V get(Object key) {
		return map.get(key);
	}

	@Override
	public boolean isEmpty() {
		return map.isEmpty();
	}

	@NonNull
	@Override
	public Set<K> keySet() {
		return map.keySet();
	}

	@Override
	public V put(K key, V value) {
		return map.put(key, value);
	}

	@Override
	public void putAll(@NonNull Map<? extends K, ? extends V> anotherMap) {
		map.putAll(anotherMap);
	}

	@Override
	public V remove(Object key) {
		return map.remove(key);
	}

	@Override
	public int size() {
		return map.size();
	}

	@Override
	public String toString() {
		return map.toString();
	}

	@NonNull
	@Override
	public Collection<V> values() {
		return map.values();
	}
}

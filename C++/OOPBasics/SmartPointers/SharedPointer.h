#pragma once

#include <assert.h>

template <typename T>
class SharedPointer {
public:
	SharedPointer(T* = nullptr);
	SharedPointer(const SharedPointer<T>&);
	SharedPointer<T>& operator=(const SharedPointer<T>&);
	~SharedPointer();

	T& operator*();
	const T& operator*() const;

	T* operator->();
	const T* operator->() const;

private:
	void deallocate();
	void check_pointer() const;

private:
	class Metadata {
	public:
		Metadata() : m_reference_count(0) {}

		void add_reference() { ++m_reference_count; }
		int release_reference() { return --m_reference_count; }

	private:
		int m_reference_count;
	};

	T* m_pointer;
	Metadata* m_metadata;
};

template <typename T>
SharedPointer<T>::SharedPointer(T* pointer)
	: m_pointer(pointer)
	, m_metadata(new Metadata()) {
	if (m_pointer != nullptr) {
		m_metadata->add_reference();
	}
}

template <typename T>
SharedPointer<T>::SharedPointer(const SharedPointer<T>& object)
	: m_pointer(object.m_pointer)
	, m_metadata(object.m_metadata) {
	if (m_pointer != nullptr) {
		assert(m_metadata != nullptr);
		m_metadata->add_reference();
	}
}

template <typename T>
SharedPointer<T>& SharedPointer<T>::operator=(const SharedPointer<T>& object) {
	if (this != &object) {
		deallocate();
		m_pointer = object.m_pointer;
		m_metadata = object.m_metadata;
		if (m_pointer != nullptr) {
			assert(m_metadata != nullptr);
			m_metadata->add_reference();
		}
	}
	return *this;
}

template <typename T>
SharedPointer<T>::~SharedPointer() {
	deallocate();
}

template <typename T>
T& SharedPointer<T>::operator*() {
	check_pointer();
	return (*m_pointer);
}

template <typename T>
const T& SharedPointer<T>::operator*() const {
	check_pointer();
	return (*m_pointer);
}

template <typename T>
T* SharedPointer<T>::operator->() {
	return m_pointer;
}

template <typename T>
const T* SharedPointer<T>::operator->() const {
	return m_pointer;
}

template <typename T>
void SharedPointer<T>::deallocate() {
	assert(m_metadata != nullptr);
	if (m_metadata->release_reference() == 0) {
		delete m_metadata;
		m_metadata = nullptr;
		delete m_pointer;
		m_pointer = nullptr;
	}
}

template <typename T>
void SharedPointer<T>::check_pointer() const {
	if (m_pointer == nullptr) {
		throw std::exception("Null pointer dereferencing.");
	}
}
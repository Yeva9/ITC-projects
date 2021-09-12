#pragma once

template <typename T>
class UniquePointer {
public:
	UniquePointer(T* = nullptr);
	UniquePointer(UniquePointer<T>&);
	UniquePointer<T>& operator=(UniquePointer<T>&);
	~UniquePointer();

	T& operator*();
	const T& operator*() const;

	T* operator->();
	const T* operator->() const;

private:
	void check_pointer() const;

private:
	T* m_pointer;
};

template <typename T>
UniquePointer<T>::UniquePointer(T* pointer)
	: m_pointer(pointer) {}

template <typename T>
UniquePointer<T>::UniquePointer(UniquePointer<T>& object)
	: m_pointer(object.m_pointer) {
	object.m_pointer = nullptr;
}

template <typename T>
UniquePointer<T>& UniquePointer<T>::operator=(UniquePointer<T>& object) {
	if (this != &object) {
		delete m_pointer;
		m_pointer = object.m_pointer;
		object.m_pointer = nullptr;
	}
	return *this;
}

template <typename T>
UniquePointer<T>::~UniquePointer() {
	delete m_pointer;
}

template <typename T>
T& UniquePointer<T>::operator*() {
	check_pointer();
	return (*m_pointer);
}

template <typename T>
const T& UniquePointer<T>::operator*() const {
	check_pointer();
	return (*m_pointer);
}

template <typename T>
T* UniquePointer<T>::operator->() {
	return m_pointer;
}

template <typename T>
const T* UniquePointer<T>::operator->() const {
	return m_pointer;
}

template <typename T>
void UniquePointer<T>::check_pointer() const {
	if (m_pointer == nullptr) {
		throw std::exception("Null pointer dereferencing.");
	}
}
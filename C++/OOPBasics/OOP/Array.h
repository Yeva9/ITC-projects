#pragma once

#include "ArrayExceptions.h"

#include <iostream>

/*Class objects are arrays with variable size.*/
template <typename T>
class Array {
	template <typename T1>
	friend std::ostream& operator<<(std::ostream&, const Array<T1>&);
	template <typename T1>
	friend std::istream& operator>>(std::istream&, Array<T1>&);

public:
	Array();	// default ctor
	Array(int, const T*);	// ctor with parameters
	Array(const Array<T>&);	// copy ctor
	Array<T>& operator=(const Array<T>&);	// assignment operator
	~Array();	// dtor

	int size() const { return m_size; }
	bool is_empty() const { return m_size == 0; }

	T& operator[](int);
	const T& operator[](int) const;

	void push_back(const T&);	// add a new element to the end of the array
	void pop_back();	// remove the last element from the array
	void insert(int, const T&);	// add a new element at the given index of the array
	void remove(int);	// remove the given element from the array

private:
	void allocate_and_initialize(const T* = nullptr);
	void deallocate();

	void check_index(int) const;

private:
	static const int MAX_SIZE = 100;

	int m_max_size;
	int m_size;
	T* m_data;
};

template <typename T>
std::ostream& operator<<(std::ostream& out, const Array<T>& object) {
	if (!object.is_empty()) {
		int i = 0;
		for (; i < object.m_size - 1; ++i) {
			out << object.m_data[i] << ' ';
		}
		out << object.m_data[i] << std::endl;
	}
	return out;
}
template <typename T>
std::istream& operator>>(std::istream& in, Array<T>& object) {
	for (int i = 0; i < object.m_size; ++i) {
		in >> object[i];
	}
	return in;
}

template <typename T>
Array<T>::Array()
	: m_max_size(MAX_SIZE)
	, m_size(0)
	, m_data(nullptr) {
	allocate_and_initialize();
}

template <typename T>
Array<T>::Array(int size, const T* data)
	: m_max_size((size > MAX_SIZE) ? size : MAX_SIZE)
	, m_size(size)
	, m_data(nullptr) {
	allocate_and_initialize(data);
}

template <typename T>
Array<T>::Array(const Array<T>& object)
	: m_max_size(object.m_max_size)
	, m_size(object.m_size)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
}

template <typename T>
Array<T>& Array<T>::operator=(const Array<T>& object) {
	if (this != &object) {
		deallocate();
		m_max_size = object.m_max_size;
		m_size = object.m_size;
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

template <typename T>
Array<T>::~Array() {
	deallocate();
}

template <typename T>
T& Array<T>::operator[](int index) {
	check_index(index);
	return m_data[index];
}

template <typename T>
const T& Array<T>::operator[](int index) const {
	check_index(index);
	return m_data[index];
}

template <typename T>
void Array<T>::push_back(const T& element) {
	if (m_size == m_max_size) {
		m_max_size *= 2;
		T* tmp = new T[m_max_size];
		for (int i = 0; i < m_size; ++i) {
			tmp[i] = m_data[i];
		}
		delete[] m_data;
		m_data = tmp;
	}
	m_data[m_size++] = element;
}

template <typename T>
void Array<T>::pop_back() {
	if (!is_empty()) {
		--m_size;
		return;
	}
	throw ArrayIsEmptyException();
}

template <typename T>
void Array<T>::insert(int index, const T& element) {
	if (index < 0) {
		throw IndexIsLessThan0Exception();
	}
	if (index >= m_size) {
		push_back(element);
	}
	else {
		if (m_size == m_max_size) {
			m_max_size *= 2;
		}
		T* tmp = new T[m_max_size];
		for (int i = 0; i < index; ++i) {
			tmp[i] = m_data[i];
		}
		tmp[index] = element;
		for (int i = index + 1; i <= m_size; ++i) {
			tmp[i] = m_data[i - 1];
		}
		delete[] m_data;
		m_data = tmp;
		++m_size;
	}
}

template <typename T>
void Array<T>::remove(int index) {
	if (index < 0) {
		throw IndexIsLessThan0Exception();
	}
	if (index >= m_size) {
		pop_back();
	}
	else {
		T* tmp = new T[m_max_size];
		for (int i = 0; i < index; ++i) {
			tmp[i] = m_data[i];
		}
		for (int i = index; i < m_size - 1; ++i) {
			tmp[i] = m_data[i + 1];
		}
		delete[] m_data;
		m_data = tmp;
		--m_size;
	}
}

template <typename T>
void Array<T>::allocate_and_initialize(const T* data) {
	m_data = new T[m_max_size] {};
	if (data != nullptr) {
		for (int i = 0; i < m_size; ++i) {
			m_data[i] = data[i];
		}
	}
}

template <typename T>
void Array<T>::deallocate() {
	delete[] m_data;
}

template <typename T>
void Array<T>::check_index(int index) const {
	if (index < 0 || index >= m_size) {
		throw IndexOutOfBoundsException();
	}
}
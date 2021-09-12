#pragma once

#include <exception>

template <typename T>
class Heap {
public:
	Heap();
	Heap(const Heap<T>&);
	Heap<T>& operator=(const Heap<T>&);
	~Heap();

	int size() const { return m_index; }
	int empty() const { return (m_index == 0); }

	const T& max() const;
	void pop();
	void push(const T&);

private:
	void allocate_and_initialize(const T* = nullptr);
	void deallocate();
	void resize();
	
	void check_empty() const;

private:
	static const int MAX_SIZE = 20;

private:
	int m_max_size;
	int m_index;
	T* m_data;
};

template <typename T>
Heap<T>::Heap()
	: m_max_size(MAX_SIZE)
	, m_index(0)
	, m_data(nullptr) {
	allocate_and_initialize();
}

template <typename T>
Heap<T>::Heap(const Heap<T>& obj)
	: m_max_size(obj.m_max_size)
	, m_index(obj.m_index)
	, m_data(nullptr) {
	allocate_and_initialize(obj.m_data);
}

template <typename T>
Heap<T>& Heap<T>::operator=(const Heap<T>& obj) {
	if (this != &obj) {
		deallocate();
		m_max_size = obj.m_max_size;
		m_index = obj.m_index;
		allocate_and_initialize(obj.m_data);
	}
	return *this;
}

template <typename T>
Heap<T>::~Heap() {
	deallocate();
}

template <typename T>
const T& Heap<T>::max() const {
	check_empty();
	return m_data[1];
}

template <typename T>
void Heap<T>::pop() {
	check_empty();
	m_data[1] = m_data[m_index--];
	int current_index{ 1 }, child_index{ 2 * current_index };
	while (child_index <= m_index) {
		if (child_index + 1 <= m_index && m_data[child_index] < m_data[child_index + 1]) {
			++child_index;
		}
		if (m_data[current_index] < m_data[child_index]) {
			std::swap(m_data[current_index], m_data[child_index]);
			current_index = child_index;
			child_index = current_index * 2;
		}
		else {
			break;
		}
	}
}

template <typename T>
void Heap<T>::push(const T& element) {
	if (m_index == m_max_size - 1) {
		resize();
	}
	m_data[++m_index] = element;
	int current_index{ m_index }, parent_index{ current_index / 2 };
	while (parent_index != 0) {
		if (m_data[current_index] > m_data[parent_index]) {
			std::swap(m_data[current_index], m_data[parent_index]);
			current_index = parent_index;
			parent_index = current_index / 2;
		}
		else {
			break;
		}
	}
}

template <typename T>
void Heap<T>::allocate_and_initialize(const T* data) {
	m_data = new T[m_max_size]{};
	if (data != nullptr) {
		for (int i = 1; i <= m_index; ++i) {
			m_data[i] = data[i];
		}
	}
}

template <typename T>
void Heap<T>::deallocate() {
	delete[] m_data;
}

template <typename T>
void Heap<T>::resize() {
	m_max_size *= 2;
	T* tmp = new T[m_max_size]{};
	for (int i = 1; i <= m_index; ++i) {
		tmp[i] = m_data[i];
	}
	deallocate();
	m_data = tmp;
}

template <typename T>
void Heap<T>::check_empty() const {
	if (empty()) {
		throw std::exception("Heap is empty.");
	}
}
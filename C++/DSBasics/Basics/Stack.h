#pragma once

#include <exception>

template <typename T>
class Stack {
public:
	Stack();
	Stack(const Stack<T>&);
	Stack<T>& operator=(const Stack<T>&);
	~Stack();

	int size() const { return (m_top + 1); }
	int is_empty() const { return (m_top == -1); }

	T& top();
	const T& top() const;
	void push(const T&);
	void pop();

private:
	void allocate_and_initialize(const T* = nullptr);
	void deallocate();
	void check_empty() const;

private:
	static const int s_max_size = 20;

private:
	int m_max_size;
	int m_top;
	T* m_data;
};

template <typename T>
Stack<T>::Stack()
	: m_max_size(s_max_size)
	, m_top(-1)
	, m_data(nullptr) {
	allocate_and_initialize();
}

template <typename T>
Stack<T>::Stack(const Stack<T>& object)
	: m_max_size(object.m_max_size)
	, m_top(object.m_top)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
}

template <typename T>
Stack<T>& Stack<T>::operator=(const Stack<T>& object) {
	if (this != &object) {
		deallocate();
		m_max_size = object.m_max_size;
		m_top = object.m_top;
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

template <typename T>
Stack<T>::~Stack() {
	deallocate();
}

template <typename T>
T& Stack<T>::top() {
	check_empty();
	return m_data[m_top];
}

template <typename T>
const T& Stack<T>::top() const {
	check_empty();
	return m_data[m_top];
}

template <typename T>
void Stack<T>::push(const T& element) {
	if (m_top == m_max_size - 1) {
		m_max_size *= 2;
		T* tmp = new T[m_max_size]{};
		for (int i = 0; i <= m_top; ++i) {
			tmp[i] = m_data[i];
		}
		delete[] m_data;
		m_data = tmp;
	}
	m_data[++m_top] = element;
}

template <typename T>
void Stack<T>::pop() {
	check_empty();
	--m_top;
}

template <typename T>
void Stack<T>::allocate_and_initialize(const T* data) {
	m_data = new T[m_max_size]{};
	if (data != nullptr) {
		for (int i = 0; i <= m_top; ++i) {
			m_data[i] = data[i];
		}
	}
}

template <typename T>
void Stack<T>::deallocate() {
	delete[] m_data;
}

template <typename T>
void Stack<T>::check_empty() const {
	if (is_empty()) {
		throw std::exception("The stack is empty.");
	}
}
#pragma once

#include <assert.h>
#include <exception>

template <typename T>
class LinkedStack {
public:
	LinkedStack();
	LinkedStack(const LinkedStack<T>&);
	LinkedStack<T>& operator=(const LinkedStack<T>&);
	~LinkedStack();

	int size() const { return m_size; }
	bool is_empty() const { return m_size == 0; }

	T& top();
	const T& top() const;
	void push(const T&);
	void pop();

private:
	template <typename T>
	struct Node {
		T m_info;
		Node<T>* m_link;

		Node(const T& info = T())
			: m_info(info)
			, m_link(nullptr) {}
	};

	void allocate(const Node<T>*);
	void deallocate();
	void check_empty() const;

private:
	int m_size;
	Node<T>* m_top;
};

template <typename T>
LinkedStack<T>::LinkedStack()
	: m_size(0)
	, m_top(nullptr) {}

template <typename T>
LinkedStack<T>::LinkedStack(const LinkedStack<T>& object)
	: m_size(object.m_size)
	, m_top(nullptr) {
	allocate(object.m_top);
}

template <typename T>
LinkedStack<T>& LinkedStack<T>::operator=(const LinkedStack<T>& object) {
	if (this != &object) {
		deallocate();
		m_size = object.m_size;
		allocate(object.m_top);
	}
	return *this;
}

template <typename T>
LinkedStack<T>::~LinkedStack() {
	deallocate();
}

template <typename T>
T& LinkedStack<T>::top() {
	check_empty();
	assert(m_top != nullptr);
	return m_top->m_info;
}

template <typename T>
const T& LinkedStack<T>::top() const {
	check_empty();
	assert(m_top != nullptr);
	return m_top->m_info;
}

template <typename T>
void LinkedStack<T>::push(const T& element) {
	Node<T>* tmp = m_top;
	m_top = new Node<T>(element);
	m_top->m_link = tmp;
	++m_size;
}

template <typename T>
void LinkedStack<T>::pop() {
	check_empty();
	assert(m_top != nullptr);
	Node<T>* tmp = m_top;
	m_top = m_top->m_link;
	delete tmp;
	--m_size;
}

template <typename T>
void LinkedStack<T>::allocate(const Node<T>* top) {
	Node<T>* t1{}, * prev{};
	const Node<T>* t2 = top;
	while (t2 != nullptr) {
		t1 = new Node<T>(t2->m_info);
		if (t2 == top) {
			m_top = t1;
		}
		if (prev != nullptr) {
			prev->m_link = t1;
		}
		prev = t1;
		t2 = t2->m_link;
	}
}

template <typename T>
void LinkedStack<T>::deallocate() {
	if (is_empty()) {
		return;
	}
	assert(m_top != nullptr);
	Node<T>* t = m_top->m_link;
	while (t != nullptr) {
		delete m_top;
		m_top = t;
		t = t->m_link;
	}
	delete m_top;
}

template <typename T>
void LinkedStack<T>::check_empty() const {
	if (is_empty()) {
		throw std::exception("The stack is empty.");
	}
}
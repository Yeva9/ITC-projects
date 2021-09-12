#pragma once

#include <assert.h>
#include <exception>

// cyclic linked list
template <typename T>
class LinkedList {
public:
	template <typename T>
	struct Node {
		T m_info;
		Node<T>* m_next;
		Node<T>* m_previous;

		Node(const T& info = T())
			: m_info(info)
			, m_next(nullptr)
			, m_previous(nullptr) {}
	};

	LinkedList();
	LinkedList(int, const T*);
	LinkedList(const LinkedList<T>&);
	LinkedList<T>& operator=(const LinkedList<T>&);
	~LinkedList();

	int size() const { return m_size; }
	bool is_empty() const { return m_size == 0; }

	// iterate
	Node<T>* head();
	const Node<T>* head() const;
	Node<T>* current();
	const Node<T>* current() const;
	void next() const;
	void previous() const;
	void reset() const;

	void insert(Node<T>*, const T&);
	void remove(Node<T>*);

private:
	void allocate(const T*);
	void allocate(const Node<T>*);
	void deallocate();
	void check_empty() const;

private:
	int m_size;
	Node<T>* m_head;
	// iteration
	mutable Node<T>* m_current;
};

template <typename T>
LinkedList<T>::LinkedList()
	: m_size(0)
	, m_head(nullptr) {}

template <typename T>
LinkedList<T>::LinkedList(int size, const T* data)
	: m_size(0)
	, m_head(nullptr) {
	allocate(data);
}

template <typename T>
LinkedList<T>::LinkedList(const LinkedList<T>& object)
	: m_size(object.m_size)
	, m_head(nullptr) {
	allocate(object.m_head);
}

template <typename T>
LinkedList<T>& LinkedList<T>::operator=(const LinkedList<T>& object) {
	if (this != &object) {
		deallocate();
		m_size = object.m_size;
		allocate(object.m_head);
	}
	return *this;
}

template <typename T>
LinkedList<T>::~LinkedList() {
	deallocate();
}

template <typename T>
LinkedList<T>::Node<T>* LinkedList<T>::head() {
	return m_head;
}

template <typename T>
const LinkedList<T>::Node<T>* LinkedList<T>::head() const {
	return m_head;
}

template <typename T>
LinkedList<T>::Node<T>* LinkedList<T>::current() {
	return m_current;
}

template <typename T>
const LinkedList<T>::Node<T>* LinkedList<T>::current() const {
	return m_current;
}

template <typename T>
void LinkedList<T>::next() const {
	assert(m_current != nullptr);
	if (m_current->m_next == nullptr) {
		throw std::exception("Current is the last element.");
	}
	return (m_current = m_current->m_next);
}

template <typename T>
void LinkedList<T>::previous() const {
	assert(m_current != nullptr);
	if (m_current->m_previous == nullptr) {
		throw std::exception("Current is the last element.");
	}
	return (m_current = m_current->m_previous);
}

template <typename T>
void LinkedList<T>::reset() const {
	m_current = m_head;
}

template <typename T>
void LinkedList<T>::insert(Node<T>* position, const T& element) {
	Node<T>* new_node = new Node<T>(element);
	if (position == nullptr) {
		new_node->m_next = m_head;
		m_head = new_node;
	}
	else {
		new_node->m_previous = position;
		new_node->m_next = position->m_next;
		if (position->m_next != nullptr) {
			position->m_next->m_previous = new_node;
		}
		position->m_next = new_node;
	}
}

template <typename T>
void LinkedList<T>::remove(Node<T>* position) {
	assert(position != nullptr);
	if (position->m_previous != nullptr) {
		position->m_previous->m_next = position->m_next;
	}
	if (position->m_next != nullptr) {
		position->m_next->m_previous = position->m_previous;
	}
}

template <typename T>
void LinkedList<T>::allocate(const T* data) {
	Node<T>* t{}, prev{};
	for (int i = 0; i < m_size; ++i) {
	}
}

template <typename T>
void LinkedList<T>::deallocate();

template <typename T>
void LinkedList<T>::check_empty() const;
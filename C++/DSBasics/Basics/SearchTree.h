#pragma once

#include "BinaryTree.h"

#include <cassert>
#include <queue>
#include <iostream>

template <typename T>
class SearchTree {
	template <typename T>
	using Node = BinaryTree::Node<T>;

	template <typename Q>
	friend std::ostream& operator<<(std::ostream&, const SearchTree<Q>&);

public:
	SearchTree();
	SearchTree(const SearchTree<T>&);
	SearchTree<T>& operator=(const SearchTree<T>&);
	~SearchTree();

	int size() const { return m_size; }
	int empty() const { return (m_size == 0); }

	Node<T>* find(const T&);
	const Node<T>* find(const T&) const;

	void insert(const T&);
	void remove(const T&);

	// iteration interface
	const Node<T>* root() const { return m_root; }
	const Node<T>* current() const { return m_current; }
	const Node<T>* next() const;
	void reset() const { m_current = m_root; }

private:
	void copy_and_allocate(const Node<T>*);
	void deallocate();

private:
	int m_size;
	Node<T>* m_root;

	// iteration implementation
	mutable Node<T>* m_current;
};

template <typename T>
std::ostream& operator<<(std::ostream& out, const SearchTree<T>& tree) {
	if (!tree.empty()) {
		std::queue<BinaryTree::Node<T>*> q;
		q.push(tree.m_root);
		BinaryTree::Node<T>* tmp{};
		while (!q.empty()) {
			tmp = q.front();
			if (tmp->has_left()) {
				q.push(tmp->m_left);
			}
			if (tmp->has_right()) {
				q.push(tmp->m_right);
			}
			out << tmp->m_info << " ";
			q.pop();
		}
	}
	out << std::endl;
	return out;
}

template <typename T>
SearchTree<T>::SearchTree()
	: m_size(0)
	, m_root(nullptr)
	, m_current(m_root) {}

template <typename T>
SearchTree<T>::SearchTree(const SearchTree<T>& obj)
	: m_size(obj.m_size)
	, m_root(nullptr) 
	, m_current(nullptr) {
	copy_and_allocate(obj.m_root);
	m_current = m_root;
}

template <typename T>
SearchTree<T>& SearchTree<T>::operator=(const SearchTree<T>& obj) {
	if (this != &obj) {
		deallocate();
		m_size = obj.m_size;
		copy_and_allocate(obj.m_root);
		m_current = m_root;
	}
	return *this;
}

template <typename T>
SearchTree<T>::~SearchTree() {
	deallocate();
}

template <typename T>
SearchTree<T>::Node<T>* SearchTree<T>::find(const T& element) {
	if (empty()) {
		return nullptr;
	}
	assert(m_root != nullptr);
	Node<T>* tmp = m_root;
	while (tmp != nullptr) {
		if (element == tmp->m_info) {
			break;
		}
		else {
			(element < tmp->m_info) ? (tmp = tmp->m_left) : (tmp = tmp->m_right);
		}
	}
	return tmp;
}

template <typename T>
const SearchTree<T>::Node<T>* SearchTree<T>::find(const T& element) const {
	if (empty()) {
		return nullptr;
	}
	assert(m_root != nullptr);
	const Node<T>* tmp = m_root;
	while (tmp != nullptr) {
		if (element == tmp->m_info) {
			break;
		}
		else {
			(element < tmp->m_info) ? (tmp = tmp->m_left) : (tmp = tmp->m_right);
		}
	}
	return tmp;
}

template <typename T>
void SearchTree<T>::insert(const T& element) {
	Node<T>* tmp = m_root, * tmp_parent{};
	while (tmp != nullptr) {
		tmp_parent = tmp;
		tmp = (element < tmp->m_info) ? (tmp->m_left) : (tmp->m_right);
	}
	assert(tmp == nullptr);
	Node<T>* to_insert = new Node<T>(element);
	if (tmp_parent == nullptr) {
		m_root = to_insert;
	}
	else {
		(element < tmp_parent->m_info) ? (tmp_parent->m_left = to_insert) : (tmp_parent->m_right = to_insert);
	}
	++m_size;
}

template <typename T>
void SearchTree<T>::remove(const T& element) {
	Node<T>* to_remove = m_root, * parent{};
	while (to_remove != nullptr && to_remove->m_info != element) {
		parent = to_remove;
		to_remove = (element < to_remove->m_info) ? (to_remove->m_left) : (to_remove->m_right);
	}
	if (to_remove == nullptr) {
		return;
	}
	if (to_remove->has_both()) {
		Node<T>* tmp = to_remove, * p = parent;
		while (tmp->has_right()) {
			p = tmp;
			tmp = tmp->m_right;
		}
		if (tmp->has_left()) {
			p = tmp;
			tmp = tmp->m_left;
		}
		else {

		}
		std::swap(to_remove->m_info, tmp->m_info);
		to_remove = tmp;
		parent = p;
	}
	if (!to_remove->is_leaf() && parent != nullptr) { // it has one child and is not the root
		Node<T>* tmp = (to_remove->has_left()) ? (to_remove->m_left) : (to_remove->m_right);
		(parent->m_left == to_remove) ? (parent->m_left = tmp) : (parent->m_right = tmp);
	}
	else if(parent != nullptr){	// it is a leaf and is not the root
		(parent->m_left == to_remove) ? (parent->m_left = nullptr) : (parent->m_right = nullptr);
	}
	delete to_remove;
	--m_size;
}

template <typename T>
const SearchTree<T>::Node<T>* SearchTree<T>::next() const {

}

template <typename T>
void SearchTree<T>::copy_and_allocate(const Node<T>* root) {
	if (root == nullptr) {
		return;
	}
	std::queue<Node<T>*> current_q, other_q;
	Node<T>* current_tmp{}, * other_tmp{};
	m_root = current_tmp = new Node<T>(root->m_info);
	current_q.push(current_tmp);
	other_q.push(root);
	while (!other_q.empty()) {
		current_tmp = current_q.front();
		other_tmp = other_q.front();
		if (other_tmp->has_left()) {
			current_tmp->m_left = new Node(other_tmp->m_left->m_info);
			current_q.push(current_tmp->m_left);
			other_q.push(other_tmp->m_left);			
		}
		if (other_tmp->has_right()) {
			current_tmp->m_right = new Node(other_tmp->m_right->m_info);
			current_q.push(current_tmp->m_right);
			other_q.push(other_tmp->m_right);
		}
		current_q->pop();
		other_q->pop();
	}
}

template <typename T>
void SearchTree<T>::deallocate() {
	if (m_root == nullptr) {
		return;
	}
	std::queue<Node<T>*> q;
	q.push(m_root);
	Node<T>* tmp{};
	while (!q.empty()) {
		tmp = q.front();
		if (tmp->has_left()) {
			q.push(tmp->m_left);
		}
		if (tmp->has_right()) {
			q.push(tmp->m_right);
		}
		q.pop();
		delete tmp;
	}
}
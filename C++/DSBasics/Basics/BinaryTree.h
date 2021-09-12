#pragma once

#include <stack>
#include <queue>

namespace BinaryTree {
	template <typename T>
	struct Node {
		T m_info;
		Node<T>* m_left;
		Node<T>* m_right;

		Node(const T& info = T())
			: m_info(info)
			, m_left(nullptr)
			, m_right(nullptr) {}

		bool is_leaf() const {
			return (m_left == nullptr && m_right == nullptr);
		}

		bool has_left() const {
			return (m_left != nullptr);
		}

		bool has_right() const {
			return (m_right != nullptr);
		}

		bool has_both() const {
			return (m_left != nullptr && m_right != nullptr);
		}
	};

	template <typename T>
	struct ExtendedNode : public Node<T> {
		ExtendedNode<T>* m_parent;

		ExtendedNode(const T& info = T())
			: Node(info)
			, m_parent(nullptr) {}

		bool is_root() const {
			return (m_parent != nullptr);
		}
	};

	template <typename T>
	using FuncNode = void (*)(Node<T>*);

	template <typename T>
	using FuncExtendedNode = void (*)(ExtendedNode<T>*);
}

namespace Traversal {
	template <typename T>
	using Node = BinaryTree::Node<T>;

	template <typename T>
	using ExtendedNode = BinaryTree::ExtendedNode<T>;

	template <typename T>
	using FuncNode = BinaryTree::FuncNode<T>;

	template <typename T>
	using FuncExtendedNode = BinaryTree::FuncExtendedNode<T>;

	template <typename T>
	void level_order_traversal(Node<T>* root, FuncNode<T> visit) {
		if (root == nullptr) {
			return;
		}
		std::queue<Node<T>*> q;
		q.push(root);
		while (!q.empty()) {
			Node<T>* tmp = q.front();
			visit(tmp);
			if (tmp->has_left()) {
				q.push(tmp->m_left);
			}
			if (tmp->has_right()) {
				q.push(tmp->m_right);
			}
			q.pop();
		}
	}

	template <typename T>
	void recursive_level_order_traversal(Node<T>* root, FuncNode<T> visit) {
		// TODO
	}

	template <typename T>
	void preorder_traversal(ExtendedNode<T>* root, FuncExtendedNode<T> visit) {
		// TODO
	}

	template <typename T>
	void recursive_preorder_traversal(Node<T>* root, FuncNode<T> visit) {
		if (root == nullptr) {
			return;
		}
		visit(root);
		if (root->m_left != nullptr) {
			recursive_preorder_traversal(root->m_left);
		}
		if (root->m_right != nullptr) {
			recursive_preorder_traversal(root->m_right);
		}
	}

	template <typename T>
	ExtendedNode<T>* inorder_first(ExtendedNode<T>* root) {
		ExtendedNode<T>* tmp = root;
		while (tmp->has_left()) {
			tmp = tmp->m_left;
		}
		return tmp;
	}

	template <typename T>
	ExtendedNode<T>* inorder_next(ExtendedNode<T>* current) {
		assert(current != nullptr);
		ExtendedNode<T>* tmp{};
		if (current->has_right()) {
			tmp = current->m_right;
			while (tmp->has_left()) {
				tmp = tmp->m_left;
			}
			return tmp;
		}
		else {
			tmp = current;
			while (!tmp->is_root()) {
				ExtendedNode<T>* p = tmp;
				tmp = tmp->m_parent;
				if (p == tmp->m_left) {
					return tmp;
				}
			}
		}
		return nullptr;
	}

	template <typename T>
	void inorder_traversal(ExtendedNode<T>* root, FuncExtendedNode<T> visit) {
		if (root == nullptr) {
			return;
		}
		ExtendedNode<T>* tmp = inorder_first(root);
		do {
			visit(tmp);
			tmp = inorder_next(tmp);
		} while (tmp != nullptr);
	}

	template <typename T>
	void inorder_traversal_with_stack(Node<T>* root, FuncNode<T> visit) {
		// TODO
	}

	template <typename T>
	void recursive_inorder_traversal(Node<T>* root, FuncNode<T> visit) {
		if (root == nullptr) {
			return;
		}
		if (root->m_left != nullptr) {
			recursive_inorder_traversal(root->m_left);
		}
		visit(root);
		if (root->m_right != nullptr) {
			recursive_inorder_traversal(root->m_right);
		}
	}

	template <typename T>
	void postorder_traversal(ExtendedNode<T>* root, FuncExtendedNode<T> visit) {
		// TODO
	}

	template <typename T>
	void recursive_postorder_traversal(Node<T>* root, FuncNode<T> visit) {
		if (root == nullptr) {
			return;
		}
		if (root->m_left != nullptr) {
			recursive_postorder_traversal(root->m_left);
		}
		if (root->m_right != nullptr) {
			recursive_postorder_traversal(root->m_right);
		}
		visit(root);
	}
}

namespace Properties {
	template <typename T>
	using Node = BinaryTree::Node<T>;

	template <typename T>
	int height(Node<T>* root) {
		if (root == nullptr || root->is_leaf()) {
			return 0;
		}
		return std::max(height(root->m_left), height(root->m_right)) + 1;
	}

	template <typename T>
	int leaf_count(Node<T>* root) {
		if (root == nullptr) {
			return 0;
		}
		if (root->is_leaf()) {
			return 1;
		}
		return leaf_count(root->m_right) + leaf_count(root->m_left) + 1;
	}
}
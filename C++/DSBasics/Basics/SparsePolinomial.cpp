#include "SparsePolinomial.h"

#include <assert.h>
#include <algorithm>

std::ostream& operator<<(std::ostream& out, const SparsePolinomial& p) {
	if (p.m_exponent != -1) {
		for (int i = 0; i < p.m_exponent; ++i) {
			double coeff = p[i];
			if (coeff != 0) {
				out << coeff << "x^" << i << " + ";
			}
		}
		out << p[p.m_exponent] << "x^" << p.m_exponent << std::endl;
	}
	return out;
}

SparsePolinomial::SparsePolinomial()
	: m_exponent(-1)
	, m_head(nullptr) {
	create_head();
}

SparsePolinomial::SparsePolinomial(const Information& information)
	: m_exponent(-1)
	, m_head(nullptr) {
	create_head();
	Node* previous = m_head, * current{};
	for (int i = 0; i < information.size(); ++i) {
		current = new Node(information[i].first, information[i].second);
		assert(previous != nullptr);
		previous->m_next = current;
		previous = previous->m_next;
	}
	if (current != nullptr) {
		current->m_next = m_head;
		assert(!information.empty());
		m_exponent = information[0].second;
	}
}

SparsePolinomial::SparsePolinomial(const SparsePolinomial& object)
	: m_exponent(object.m_exponent)
	, m_head(nullptr) {
	create_head();
	allocate_from_object(object);
}

SparsePolinomial& SparsePolinomial::operator=(const SparsePolinomial& object) {
	if (this != &object) {
		deallocate(false);
		m_exponent = object.m_exponent;
		allocate_from_object(object);
	}
	return *this;
}

SparsePolinomial::~SparsePolinomial() {
	deallocate();
}

const double& SparsePolinomial::operator[](int e) const {
	check_exponent(e);
	assert(m_head != nullptr);
	Node* current = m_head->m_next;
	while (current != m_head) {
		if (current->m_exponent == e) {
			return current->m_coeff;
		}
		current = current->m_next;
	}
	return 0;
}

SparsePolinomial& SparsePolinomial::operator+=(const SparsePolinomial& object) {
	assert(m_head != nullptr);
	assert(object.m_head != nullptr);
	Node* previous = m_head, * this_current = m_head->m_next;
	const Node* object_current = object.m_head->m_next;
	while (object_current != object.m_head) {
		if (this_current->m_exponent == object_current->m_exponent) {
			this_current->m_coeff += object_current->m_coeff;
			if (this_current->m_coeff == 0) {
				previous->m_next = this_current->m_next;
				delete this_current;
				this_current = previous;
			}
			previous = this_current;
			this_current = this_current->m_next;
			object_current = object_current->m_next;
		}
		else if(this_current->m_exponent < object_current->m_exponent) {
			Node* tmp = new Node(object_current->m_coeff, object_current->m_exponent);
			tmp->m_next = this_current;
			previous->m_next = tmp;
			previous = tmp;
			object_current = object_current->m_next;
		}
		else {
			previous = this_current;
			this_current = this_current->m_next;
		}
	}
	m_exponent = m_head->m_next->m_exponent;
	return *this;
}

SparsePolinomial& SparsePolinomial::operator*=(const SparsePolinomial& object) {
	// TODO add implementation
	return *this;
}

SparsePolinomial& SparsePolinomial::operator*=(const double& coeff) {
	if (coeff == 0) {
		deallocate(false);
		m_exponent = -1;
	}
	else {
		assert(m_head != nullptr);
		Node* current = m_head->m_next;
		while (current != m_head) {
			current->m_coeff *= coeff;
			current = current->m_next;
		}
	}
	return *this;
}

SparsePolinomial& SparsePolinomial::derivative() {
	if (m_exponent != -1) {
		assert(m_head != nullptr);
		Node* previous = m_head, * current = m_head->m_next;
		while (current->m_exponent != 0 && current != m_head) {
			current->m_coeff *= (current->m_exponent)--;
			previous = current;
			current = current->m_next;
		}
		if (current->m_exponent == 0) {
			previous->m_next = m_head;
			delete current;
		}
		--m_exponent;
	}
	return *this;
}

double SparsePolinomial::calculate_value(const double& value) const {
	assert(m_head != nullptr);
	double result = 0;
	const Node* current = m_head->m_next;
	while (current != m_head) {
		result += current->m_coeff * std::pow(value, current->m_exponent);
		current = current->m_next;
	}
	return result;
}

void SparsePolinomial::create_head() {
	m_head = new Node(0, -1);
	m_head->m_next = m_head;
}

void SparsePolinomial::allocate_from_object(const SparsePolinomial& object) {
	assert(m_head != nullptr);
	Node* previous = m_head, * current{};
	const Node* object_current = object.m_head->m_next;
	while (object_current != object.m_head) {
		current = new Node(object_current->m_coeff, object_current->m_exponent);
		assert(previous != nullptr);
		previous->m_next = current;
		previous = previous->m_next;
		object_current = object_current->m_next;
	}
	if (current != nullptr) {
		current->m_next = m_head;
	}
}

void SparsePolinomial::deallocate(bool all) {
	assert(m_head != nullptr);
	Node* previous = m_head, * current = m_head->m_next;
	while (current != m_head) {
		previous = current;
		current = current->m_next;
		delete previous;
	}
	if(all) {
		delete m_head;
	}
	else {
		m_head->m_next = m_head;
	}
}

void SparsePolinomial::check_exponent(int e) const {
	if (e < 0 || e > m_exponent) {
		throw std::exception("Not correct exponent is given");
	}
}

SparsePolinomial operator+(SparsePolinomial p1, const SparsePolinomial& p2) {
	return p1 += p2;
}

SparsePolinomial operator*(SparsePolinomial p1, const SparsePolinomial& p2) {
	return p1 *= p2;
}

SparsePolinomial operator*(SparsePolinomial p, const double& coeff) {
	return p *= coeff;
}
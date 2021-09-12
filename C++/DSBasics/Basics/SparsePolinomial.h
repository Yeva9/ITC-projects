#pragma once

#include <iostream>
#include <vector>

class SparsePolinomial {
	friend std::ostream& operator<<(std::ostream&, const SparsePolinomial&);

public:
	typedef std::vector<std::pair<double, int>> Information;

	SparsePolinomial();
	SparsePolinomial(const Information&);
	SparsePolinomial(const SparsePolinomial&);
	SparsePolinomial& operator=(const SparsePolinomial&);
	~SparsePolinomial();

	int get_exponent() const { return m_exponent; }

	const double& operator[](int) const;

	SparsePolinomial& operator+=(const SparsePolinomial&);
	SparsePolinomial& operator*=(const SparsePolinomial&);
	SparsePolinomial& operator*=(const double&);

	SparsePolinomial& derivative();
	double calculate_value(const double&) const;

private:
	void create_head();
	void allocate_from_object(const SparsePolinomial&);
	void deallocate(bool = true);
	void check_exponent(int) const;

private:
	struct Node {
		double m_coeff;
		int m_exponent;
		Node* m_next;

		Node(double coeff, int exponent)
			: m_coeff(coeff)
			, m_exponent(exponent)
			, m_next(nullptr) {}
	};

	int m_exponent;
	Node* m_head;
};

SparsePolinomial operator+(SparsePolinomial, const SparsePolinomial&);
SparsePolinomial operator*(SparsePolinomial, const SparsePolinomial&);
SparsePolinomial operator*(SparsePolinomial, const double&);
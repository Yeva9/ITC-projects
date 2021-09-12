#include "Testing.h"

#include <iostream>
#include <exception>

class Function {
public:
	Function() {}
	Function(const Function&) = delete;
	Function& operator=(const Function&) = delete;
	virtual ~Function() {}

	double operator()(const double& x) {
		return calculate(x);
	}

protected:
	virtual Function* clone(const Function*) const = 0;
	virtual double calculate(const double&) const = 0;
};

class Linear : public Function {
public:
	Linear(const double& a, const double& b)
		: m_a(a)
		, m_b(b) {}
private:
	double m_a;
	double m_b;
};

class Sum : public Function {
public:
	Sum(const Function* left, const Function* right) {
		m_left = left->clone();
		m_right = right->clone();
	}

private:
	Function* m_left;
	Function* m_right;
};

int main() {

	/*std::cout << "**** Test for Array class ****" << std::endl;
	Testing::test_for_array();

	std::cout << std::endl << "**** Test for BitVector class ****" << std::endl;
	Testing::test_for_bitvector();

	std::cout << std::endl << "**** Test for HugeInteger class ****" << std::endl;
	Testing::test_for_hugeinteger();

	std::cout << std::endl << "**** Test for MultiSet class ****" << std::endl;
	Testing::test_for_multiset();

	std::cout << std::endl << "**** Test for Set class ****" << std::endl;
	Testing::test_for_set();

	std::cout << std::endl << "**** Test for String class ****" << std::endl;
	Testing::test_for_string();

	std::cout << std::endl << "**** Test for Table class ****" << std::endl;
	Testing::test_for_table();

	std::cout << std::endl << "**** Test for MyVector class ****" << std::endl;
	Testing::test_for_myvector();*/

	return 0;
}
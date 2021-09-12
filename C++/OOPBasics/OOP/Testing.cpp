#include "Testing.h"

#include "Array.h"
#include "ArrayExceptions.h"
#include "BitVector.h"
#include "HugeInteger.h"
#include "MultiSet.h"
#include "Set.h"
#include "String.h"
#include "Table.h"
#include "Vector.h"

void Testing::test_for_array() {
	// testing default ctor, push_back and pop_back
	Array<int> a1;
	a1.push_back(1);
	a1.push_back(2);
	a1.push_back(3);
	a1.push_back(4);
	std::cout << "after 4 push_back calls a1 is: " << a1;
	try {
		a1.pop_back();
		a1.pop_back();
	}
	catch (const ArrayIsEmptyException& e) {
		std::cout << "Exception is thrown while pop_back(): " << e.what() << std::endl;
	}
	std::cout << "after 2 pop_back calls a1 is: " << a1;

	// testing ctor, insert and remove
	const int n = 5;
	int a[5] = { 5, 4, 3, 2, 1 };
	Array<int> a2(5, a);
	std::cout << "a2 is: " << a2;
	try {
		a2.insert(2, 100);
		a2.insert(5, 100);
		a2.insert(10, 100);
	}
	catch (const IndexIsLessThan0Exception& e) {
		std::cout << "Exception is thrown while insert(): " << e.what() << std::endl;
	}
	std::cout << "after 3 inserts a2 is: " << a2;
	try {
		a2.remove(10);
		a2.remove(5);
		a2.remove(2);
	}
	catch (const IndexIsLessThan0Exception& e) {
		std::cout << "Exception is thrown while remove(): " << e.what() << std::endl;
	}
	std::cout << "after 3 removes a2 is: " << a2;

	// testing copy ctor
	Array<int> a3(a2);
	a3.push_back(0);
	std::cout << "a3 is: " << a3;

	// testing assignment operator
	a1 = a3;
	std::cout << "after a1 = a3 a1 is: " << a1;

	// testing size and is_empty
	Array<int> a4;
	std::cout << "a1 size is: " << a1.size() << ", a2 size is: " << a2.size() 
		      << ", a3 size is:" << a3.size() << ", a4 size is:" << a4.size() << std::endl;
	std::cout << "is a1 empty: " << a1.is_empty() << ", is a2 empty:" << a2.is_empty() 
		      << ", is a3 empty:" << a3.is_empty() << ", is a4 empty:" << a4.is_empty() << std::endl;

	// testing i/o operators
	std::cout << "insert a1" << std::endl;
	std::cin >> a1;
	std::cout << "a1 is: " << a1;
}

void Testing::test_for_bitvector() {
	// testing ctor, operator[] and ~
	BitVector v1(6);
	std::cout << "v1 is: " << v1;
	v1[1] = true;
	v1[4] = true;
	std::cout << "after changes v1 is: " << v1;
	~v1;
	std::cout << "after ~ v1 is: " << v1;

	// testing ctor, &, | and ^
	bool b[6] = { true, true, false, true, false, true };
	BitVector v2(6, b);
	std::cout << "v2 is: " << v2;
	std::cout << "v1 & v2 is: " << (v1 & v2);
	std::cout << "v1 | v2 is: " << (v1 | v2);
	std::cout << "v1 ^ v2 is: " << (v1 ^ v2);

	// testing copy ctor, testing << and >>
	BitVector v3(v2);
	std::cout << "v3 is: " << v3;
	v3 <<= 3;
	std::cout << "after v3 <<= 3 v3 is: " << v3;
	v3 >>= 2;
	std::cout << "after v3 >>= 2 v3 is: " << v3;
	v1 <<= 10;
	std::cout << "after v1 <<= 10 v1 is: " << v1;
	v2 >>= 10;
	std::cout << "after v2 >>= 10 v2 is: " << v2;

	// testing operator assignment and size
	v1 = v3;
	std::cout << "after v1 = v3 v1 is: " << v1;
	std::cout << "v1 size is: " << v1.size() << ", v2 size is: " << v2.size() 
		      << ", v3 size is: " << v3.size() << std::endl;

	// testing i/o operators
	std::cout << "insert v3" << std::endl;
	std::cin >> v3;
	std::cout << "v3 is: " << v3;
}

void Testing::test_for_hugeinteger() {

}

void Testing::test_for_multiset() {
	// testing ctor and operator<<
	int a[15] = { 3, 6, 1, 3, 8, 9, 9, 8, 8, 2, 11, 14, 2, 14, 2};
	MultiSet m1(15, a);
	std::cout << "m1 is: " << m1;

	// testing contains
	std::cout << "m1 contains 20: " << m1.contains(20) << std::endl;
	std::cout << "m1 contains 2: "  << m1.contains(2) << std::endl;

	// testing copy ctor and operator=
	MultiSet m2(m1);
	std::cout << "m2 is: " << m2;
	int b[7] = { 2, 2, 2, 2 };
	MultiSet m3(7, b);
	std::cout << "m3 is: " << m3;
	m2 = m3;
	std::cout << "after m2 = m3 m2 is: " << m2;

	// testing is_sub_set, operator==, operator&=, operator|=, operator-=
	int c[7] = { 3, 6, 1, 3, 8, 9, 9};
	MultiSet m4(7, c);
	std::cout << "m4 is: " << m4;
	std::cout << "is m4 subset for m1: " << m1.is_sub_set(m4) << std::endl;
	std::cout << "is m2 subset for m1: " << m1.is_sub_set(m2) << std::endl;
	std::cout << "are m1 and m2 equal: " << (m1 == m2) << std::endl;
	std::cout << "are m2 and m3 equal: " << (m3 == m2) << std::endl;
	m2 &= m1;
	std::cout << "after m2 &= m1 m2 is: " << m2;
	m3 |= m1;
	std::cout << "after m3 |= m1 m3 is: " << m3;
	m1 -= m4;
	std::cout << "after m1 -= m4 m1 is: " << m1;
}

void Testing::test_for_set() {
	// testing ctor and operator<<
	int a[15] = { 3, 6, 1, 3, 8, 9, 9, 8, 8, 2, 11, 14, 2, 14, 2 };
	Set s1(15, a);
	std::cout << "s1 is: " << s1;

	// testing contains
	std::cout << "s1 contains 20: " << s1.contains(20) << std::endl;
	std::cout << "s1 contains 2: " << s1.contains(2) << std::endl;

	// testing copy ctor and operator=
	Set s2(s1);
	std::cout << "s2 is: " << s2;
	int b[7] = { 2, 2, 2, 2 };
	Set s3(7, b);
	std::cout << "s3 is: " << s3;
	s2 = s3;
	std::cout << "after s2 = s3 s2 is: " << s2;

	// testing is_sub_set, operator==, operator&=, operator|=, operator-=
	int c[7] = { 3, 6, 1, 3, 8, 9, 9 };
	Set s4(7, c);
	std::cout << "s4 is: " << s4;
	std::cout << "is s4 subset for s1: " << s1.is_sub_set(s4) << std::endl;
	std::cout << "is s2 subset for s1: " << s1.is_sub_set(s2) << std::endl;
	std::cout << "are s1 and s2 equal: " << (s1 == s2) << std::endl;
	std::cout << "are s2 and s3 equal: " << (s3 == s2) << std::endl;
	s2 &= s1;
	std::cout << "after s2 &= s1 s2 is: " << s2;
	s3 |= s1;
	std::cout << "after s3 |= s1 s3 is: " << s3;
	s1 -= s4;
	std::cout << "after s1 -= s4 s1 is: " << s1;
}

void Testing::test_for_string() {

}

void Testing::test_for_table() {
	// testing ctors and operator<<
	Table<int> t1(3, 4);
	std::cout << "t1 is: " << std::endl << t1;
	int** a = new int* [3];
	for (int i = 0; i < 3; ++i) {
		a[i] = new int[4]{ 1, 2, 3, 4 };
	}
	Table<int> t2(3, 4, a);
	std::cout << "t2 is: " << std::endl << t2;

	// testing copy ctor
	Table<int> t3(t1);
	std::cout << "t3 is: " << std::endl << t3;

	// testing operator()
	t1(1, 2) = 5;
	t1(2, 3) = 8;
	t1(0, 0) = 1;
	std::cout << "after changes t1 is: " << std::endl << t1;

	// testing operator+=, operator-= and operator *=
	t1 += t2;
	std::cout << "after t1 += t2 t1 is: " << std::endl << t1;
	t1 -= t2;
	std::cout << "after t1 -= t2 t1 is: " << std::endl << t1;
	Table<int> t4(4, 2);
	std::cout << "t4 is: " << std::endl << t4;
	t1 *= t4;
	std::cout << "after t1 *= t4 t1 is: " << std::endl << t1;

	// testing i/o operators
	std::cout << "insert t2" << std::endl;
	std::cin >> t2;
	std::cout << "t2 is: " << std::endl << t2;
}

void Testing::test_for_myvector() {
	// testing ctors and operator<<
	MyVector v1(4);
	std::cout << "v1 is: " << v1;
	int a[4] = { 1, 2, 4, 6 };
	MyVector v2(4, a);
	std::cout << "v2 is: " << v2;

	// testing copy ctor
	MyVector v3(v2);
	std::cout << "v3 is: " << v3;

	// testing operator[], operator +=, operator-=, operator*, distance
	v3[2] = 10;
	std::cout << "after changes v3 is: " << v3;
	v1 += v3;
	std::cout << "after v1 += v3 v1 is: " << v1;
	v1 -= v3;
	std::cout << "after v1 -= v3 v1 is: " << v1;
	std::cout << "v1 * v3 is: " << (v1 * v3) << std::endl;
	std::cout << "distance between v1 and v3 is: " << v1.distance(v3) << std::endl;
	std::cout << "is v1 equal to v2: " << (v1 == v2) << std::endl;

	// testing i/o operators
	std::cout << "insert v2" << std::endl;
	std::cin >> v2;
	std::cout << "v2 is: " << v2;
}
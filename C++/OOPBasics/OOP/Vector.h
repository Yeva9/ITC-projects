#pragma once

#include <iostream>

/*Class objects are n-dimesional vectors.*/
class MyVector {
	friend std::ostream& operator<<(std::ostream&, const MyVector&);
	friend std::istream& operator>>(std::istream&, MyVector&);

public:
	explicit MyVector(int);	// n >= 2 ctor with parameters
	MyVector(int, const int*);	// ctor with parameters
	MyVector(const MyVector&);	// copy ctor
	MyVector& operator=(const MyVector&);	// assignment operator
	~MyVector();	// dtor

	int dimension() const { return m_dimension; }
	double distance(const MyVector&) const;	// distance of *this and given MyVector object

	int& operator[](int);
	const int& operator[](int) const;

	MyVector& operator+=(const MyVector&);
	MyVector& operator-=(const MyVector&);
	int operator*(const MyVector&);

	bool operator==(const MyVector&) const;

private:
	void allocate_and_initialize(const int* = nullptr);
	void deallocate();

	void check_dimension(int) const;
	void check_size(const MyVector&) const;

private:
	int m_dimension;
	int* m_data;
};

MyVector operator+(MyVector, const MyVector&);
MyVector operator-(MyVector, const MyVector&);

bool operator!=(const MyVector&, const MyVector&);
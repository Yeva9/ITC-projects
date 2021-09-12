#include "Vector.h"

std::ostream& operator<<(std::ostream& out, const MyVector& object) {
	out << '(';
	for (int i = 0; i < object.m_dimension - 1; ++i) {
		out << object.m_data[i] << ", ";
	}
	out << object.m_data[object.m_dimension - 1] << ')' << std::endl;
	return out;
}

std::istream& operator>>(std::istream& in, MyVector& object) {
	for (int i = 0; i < object.m_dimension; ++i) {
		in >> object.m_data[i];
	}
	return in;
}

MyVector::MyVector(int dimension)
	: m_dimension(dimension)
	, m_data(nullptr) {
	allocate_and_initialize();
}

MyVector::MyVector(int dimension, const int* data)
	: m_dimension(dimension)
	, m_data(nullptr) {
	allocate_and_initialize(data);
}

MyVector::MyVector(const MyVector& object)
	: m_dimension(object.m_dimension)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
}

MyVector& MyVector::operator=(const MyVector& object) {
	if (this != &object) {
		deallocate();
		m_dimension = object.m_dimension;
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

MyVector::~MyVector() {
	deallocate();
}

double MyVector::distance(const MyVector& object) const {
	check_size(object);
	double x{}, y{};
	for (int i = 0; i < m_dimension; ++i) {
		y = (object.m_data[i] - m_data[i]);
		x += y * y;
	}
	return pow(x, 1.0 / 2);
}

int& MyVector::operator[](int dimension) {
	check_dimension(dimension);
	return m_data[dimension];
}

const int& MyVector::operator[](int dimension) const {
	check_dimension(dimension);
	return m_data[dimension];
}

MyVector& MyVector::operator+=(const MyVector& object) {
	check_size(object);
	for (int i = 0; i < m_dimension; ++i) {
		m_data[i] += object.m_data[i];
	}
	return *this;
}

MyVector& MyVector::operator-=(const MyVector& object) {
	check_size(object);
	for (int i = 0; i < m_dimension; ++i) {
		m_data[i] -= object.m_data[i];
	}
	return *this;
}

int MyVector::operator*(const MyVector& object) {
	check_size(object);
	int x{};
	for (int i = 0; i < m_dimension; ++i) {
		x += m_data[i] * object.m_data[i];
	}
	return x;
}

bool MyVector::operator==(const MyVector& object) const {
	if (m_dimension != object.m_dimension) {
		return false;
	}
	for (int i = 0; i < m_dimension; ++i) {
		if (m_data[i] != object.m_data[i]) {
			return false;
		}
	}
	return true;
}

void MyVector::allocate_and_initialize(const int* data) {
	m_data = new int[m_dimension] {};
	if (data != nullptr) {
		for (int i = 0; i < m_dimension; ++i) {
			m_data[i] = data[i];
		}
	}
}

void MyVector::deallocate() {
	delete[] m_data;
}

void MyVector::check_dimension(int dimension) const {
	if (dimension < 0 || dimension >= m_dimension) {
		throw std::exception("Index is out of bounds.");
	}
}

void MyVector::check_size(const MyVector& object) const {
	if (m_dimension != object.m_dimension) {
		throw std::exception("Not correspondig dimensions of MyVectors.");
	}
}

MyVector operator+(MyVector v1, const MyVector& v2) {
	return v1 += v2;
}

MyVector operator-(MyVector v1, const MyVector& v2) {
	return v1 -= v2;
}

bool operator!=(const MyVector& v1, const MyVector& v2) {
	return !(v1 == v2);
}
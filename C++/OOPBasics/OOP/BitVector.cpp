#include "BitVector.h"

std::ostream& operator<<(std::ostream& out, const BitVector& object) {
	for (int i = 0; i < object.m_size; ++i) {
		out << object.m_data[i];
	}
	out << std::endl;
	return out;
}

std::istream& operator>>(std::istream& in, BitVector& object) {
	for (int i = 0; i < object.m_size; ++i) {
		in >> object.m_data[i];
	}
	return in;
}

BitVector::BitVector(int size)
	: m_size(size)
	, m_data(nullptr) {
	allocate_and_initialize();
}

BitVector::BitVector(int size, const bool* data)
	: m_size(size)
	, m_data(nullptr) {
	allocate_and_initialize(data);
}

BitVector::BitVector(const BitVector& object)
	: m_size(object.m_size)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
}

BitVector& BitVector::operator=(const BitVector& object) {
	if (this != &object) {
		deallocate();
		m_size = object.m_size;
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

BitVector::~BitVector() {
	deallocate();
}

BitVector& BitVector::operator&=(const BitVector& object) {
	check_size_correct(object);
	for (int i = 0; i < m_size; ++i) {
		m_data[i] = m_data[i] && object.m_data[i];
	}
	return *this;
}

BitVector& BitVector::operator|=(const BitVector& object) {
	check_size_correct(object);
	for (int i = 0; i < m_size; ++i) {
		m_data[i] = m_data[i] || object.m_data[i];
	}
	return *this;
}

BitVector& BitVector::operator^=(const BitVector& object) {
	check_size_correct(object);
	for (int i = 0; i < m_size; ++i) {
		m_data[i] = (m_data[i] != object.m_data[i]);
	}
	return *this;
}

BitVector& BitVector::operator<<=(int n) {
	if (n > m_size) {
		n = m_size;
	}
	int i = 0;
	for (; i < m_size - n; ++i) {
		m_data[i] = m_data[i + n];
	}
	for (; i < m_size; ++i) {
		m_data[i] = false;
	}
	return *this;
}

BitVector& BitVector::operator>>=(int n) {
	if (n > m_size) {
		n = m_size;
	}
	int i = m_size - 1;
	for (; i >= n; --i) {
		m_data[i] = m_data[i - n];
	}
	for (; i >= 0; --i) {
		m_data[i] = false;
	}
	return *this;
}

BitVector& BitVector::operator~() {
	for (int i = 0; i < m_size; ++i) {
		m_data[i] = !m_data[i];
	}
	return *this;
}

bool& BitVector::operator[](int index) {
	check_index(index);
	return m_data[index];
}

const bool& BitVector::operator[](int index) const {
	check_index(index);
	return m_data[index];
}

void BitVector::allocate_and_initialize(const bool* data) {
	m_data = new bool[m_size] {};
	if (data != nullptr) {
		for (int i = 0; i < m_size; ++i) {
			m_data[i] = data[i];
		}
	}
}

void BitVector::deallocate() {
	delete[] m_data;
}

void BitVector::check_index(int index) const {
	if (index < 0 || index >= m_size) {
		throw std::exception("Index is out of bounds.");
	}
}

void BitVector::check_size_correct(const BitVector& object) const {
	if (m_size != object.m_size) {
		throw std::exception("Not correspondig sizes of arguments.");
	}
}

BitVector operator&(BitVector bv1, const BitVector& bv2) {
	return bv1 &= bv2;
}

BitVector operator|(BitVector bv1, const BitVector& bv2) {
	return bv1 |= bv2;
}

BitVector operator^(BitVector bv1, const BitVector& bv2) {
	return bv1 ^= bv2;
}

BitVector operator<<(BitVector bv, int n) {
	return bv <<= n;
}

BitVector operator>>(BitVector bv, int n) {
	return bv >>= n;
}
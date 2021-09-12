#include "HugeInteger.h"

#include <limits>
#include <algorithm>

std::ostream& operator<<(std::ostream& out, const HugeInteger& object) {
	for (int i = object.m_max_length - object.m_length; i < object.m_max_length; ++i) {
		out << object.m_data[i];
	}
	out << std::endl;
	return out;
}

// TODO implement
std::istream& operator>>(std::istream& in, HugeInteger& object) {
	return in;
}

const int MAX_LENGTH = (std::numeric_limits<unsigned int>().digits10 + 1) * 2;

int HugeInteger::s_created_object_count = 0;

namespace {
	int get_int(char c) {
		return c - '0';
	}

	char get_char(int i) {
		return i + '0';
	}
}

HugeInteger::HugeInteger(unsigned int value)
	: m_max_length(MAX_LENGTH)
	, m_length(0)
	, m_data(nullptr) {
	m_data = new char[m_max_length] {};
	if (value == 0) {
		m_length = 1;
		m_data[m_max_length - 1] = get_char(0);
	}
	for (int i = m_max_length - 1; value != 0; --i, value /= 10) {
		m_data[i] = get_char(value % 10);
		++m_length;
	}
	++s_created_object_count;
}

HugeInteger::HugeInteger(const char* data)
	: m_max_length(0)
	, m_length(0)
	, m_data(nullptr) {
	const unsigned int length = (unsigned int)strlen(data);
	m_max_length = (length > MAX_LENGTH) ? length : MAX_LENGTH;
	m_length = length;
	m_data = new char[m_max_length] {};
	for (int i = length - 1, j = m_max_length - 1; i >= 0; --i, --j) {
		m_data[j] = data[i];
	}
	++s_created_object_count;
}

HugeInteger::HugeInteger(const HugeInteger& object)
	: m_max_length(object.m_max_length)
	, m_length(object.m_length)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
	++s_created_object_count;
}

HugeInteger& HugeInteger::operator=(const HugeInteger& object) {
	if (this != &object) {
		deallocate();
		m_max_length = object.m_max_length;
		m_length = object.m_length;
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

HugeInteger::~HugeInteger() {
	deallocate();
}

HugeInteger& HugeInteger::operator+=(const HugeInteger& object) {
	if (std::max(m_max_length, object.m_max_length) + 1 > m_max_length) {
		resize(object.m_max_length * 2);
	}
	int first_index = m_max_length - m_length;
	int first_index_object = object.m_max_length - object.m_length;
	int min_index = m_max_length - std::max(m_length, object.m_length);
	int in_mind{}, sum{}, d{}, d_object{};
	int i = m_max_length - 1, j = object.m_max_length - 1;
	for (; i >= min_index; --i, --j) {
		d = (i >= first_index) ? get_int(m_data[i]) : 0;
		d_object = (j >= first_index_object) ? get_int(object.m_data[j]) : 0;
		sum = d + d_object + in_mind;
		m_data[i] = get_char(sum % 10);
		in_mind = sum / 10;
	}
	if (in_mind != 0) {
		m_data[i] = '1';
	}
	m_length = m_max_length - i;
	return *this;
}

HugeInteger& HugeInteger::operator++() {
	int first_index = m_max_length - m_length;
	int i = m_max_length - 1;
	while (i >= first_index && m_data[i] == '9') {
		m_data[i--] = '0';
	}
	if (i < first_index) {
		++m_length;
		if (i < 0) {
			resize(m_max_length * 2);
			i = m_max_length - m_length;
		}
		m_data[i] = '1';
	}
	else {
		++m_data[i];
	}
	return *this;
}

HugeInteger HugeInteger::operator++(int) {
	HugeInteger tmp(*this);
	operator++();
	return tmp;
}

bool HugeInteger::operator==(const HugeInteger& object) const {
	if (this == &object) {
		return true;
	}
	if (m_length != object.m_length) {
		return false;
	}
	for (int i = m_max_length - m_length, j = object.m_max_length - object.m_length; i < m_max_length; ++i, ++j) {
		if (m_data[i] != object.m_data[j]) {
			return false;
		}
	}
	return true;
}

bool HugeInteger::operator<(const HugeInteger& object) const {
	if (this == &object) {
		return false;
	}
	if (m_length < object.m_length) {
		return true;
	}
	if (m_length > object.m_length) {
		return false;
	}
	for (int i = m_max_length - m_length, j = object.m_max_length - object.m_length; i < m_max_length; ++i, ++j) {
		if (m_data[i] < object.m_data[i]) {
			return true;
		}
	}
	return false;
}

HugeInteger::operator unsigned int() {
	const int digits = std::numeric_limits<unsigned int>().digits10 + 1;
	if (m_length > digits) {
		throw std::exception("HugeInteger is too huge.");
	}
	unsigned int result = 0;
	for (int i = m_max_length - m_length; i < m_max_length; ++i) {
		result = result * 10 + get_int(m_data[i]);
	}
	return result;
}

void HugeInteger::allocate_and_initialize(const char* data) {
	m_data = new char[m_max_length] {};
	for (int i = m_max_length - m_length; i < m_max_length; ++i) {
		m_data[i] = data[i];
	}
}

void HugeInteger::deallocate() {
	delete[] m_data;
}

void HugeInteger::resize(int new_length) {
	int old_max_length = m_max_length;
	m_max_length = new_length;
	char* tmp = new char[m_max_length] {};
	for (int i = m_max_length - m_length, j = old_max_length - m_length; i < m_max_length; ++i, ++j) {
		tmp[i] = m_data[j];
	}
	delete[] m_data;
	m_data = tmp;
}

HugeInteger operator+(HugeInteger I1, const HugeInteger& I2) {
	return I1 += I2;
}

bool operator!=(const HugeInteger& I1, const HugeInteger& I2) {
	return !(I1 == I2);
}

bool operator<=(const HugeInteger& I1, const HugeInteger& I2) {
	return (I1 == I2) || (I1 < I2);
}

bool operator>(const HugeInteger& I1, const HugeInteger& I2) {
	return !(I1 <= I2);
}

bool operator>=(const HugeInteger& I1, const HugeInteger& I2) {
	return (I1 == I2) || (I1 > I2);
}
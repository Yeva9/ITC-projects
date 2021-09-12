#include "MultiSet.h"

#include <algorithm>

std::ostream& operator<<(std::ostream& out, const MultiSet& object) {
	for (int i = 0; i < MultiSet::s_set_limit; ++i) {
		if (object.m_data[i] != 0) {
			for (int j = 0; j < object.m_data[i]; ++j) {
				out << i << ' ';
			}
		}
	}
	out << std::endl;
	return out;
}

MultiSet::MultiSet()
	: m_size(0)
	, m_data(nullptr) {
	m_data = new int[s_set_limit] {};
}

MultiSet::MultiSet(int size, const int* data)
	: m_size(size)
	, m_data(nullptr) {
	m_data = new int[s_set_limit] {};
	for (int i = 0; i < m_size; ++i) {
		++m_data[data[i]];
	}
}

MultiSet::MultiSet(const MultiSet& object)
	: m_size(object.m_size)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
}

MultiSet::~MultiSet() {
	deallocate();
}

MultiSet& MultiSet::operator=(const MultiSet& object) {
	if (this != &object) {
		deallocate();
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

bool MultiSet::contains(int element) const {
	check_size(element);
	return (m_data[element] != 0);
}

bool MultiSet::is_sub_set(const MultiSet& object) const {
	for (int i = 0; i < s_set_limit; ++i) {
		if (m_data[i] < object.m_data[i]) {
			return false;
		}
	}
	return true;
}

MultiSet& MultiSet::operator&=(const MultiSet& object) {
	m_size = 0;
	for (int i = 0; i < s_set_limit; ++i) {
		m_data[i] = std::min(m_data[i], object.m_data[i]);
		m_size += m_data[i];
	}
	return *this;	
}

MultiSet& MultiSet::operator|=(const MultiSet& object) {	
	m_size = 0;
	for (int i = 0; i < s_set_limit; ++i) {
		m_data[i] += object.m_data[i];
		m_size += m_data[i];
	}
	return *this;
}

MultiSet& MultiSet::operator-=(const MultiSet& object) {
	m_size = 0;
	for (int i = 0; i < s_set_limit; ++i) {
		if (m_data[i] <= object.m_data[i]) {
			m_data[i] = 0;
		}
		else {
			m_data[i] -= object.m_data[i];
		}
		m_size += m_data[i];
	}
	return *this;
}

bool MultiSet::operator==(const MultiSet& object) const {
	for (int i = 0; i < s_set_limit; ++i) {
		if (m_data[i] != object.m_data[i]) {
			return false;
		}
	}
	return true;
}

void MultiSet::allocate_and_initialize(const int* data) {
	m_data = new int[s_set_limit] {};
	for (int i = 0; i < s_set_limit; ++i) {
		m_data[i] = data[i];
	}
}

void MultiSet::deallocate() {
	delete[] m_data;
}

void MultiSet::check_size(int element) const {
	if (element < 0 || element >= s_set_limit) {
		throw std::exception("Element is out of limits.");
	}
}

MultiSet operator&(MultiSet ms1, const MultiSet& ms2) {
	return ms1 &= ms2;
}

MultiSet operator|(MultiSet ms1, const MultiSet& ms2) {
	return ms1 |= ms2;
}

MultiSet operator-(MultiSet ms1, const MultiSet& ms2) {
	return ms1 -= ms2;
}

bool operator!=(const MultiSet& ms1, const MultiSet& ms2) {
	return !(ms1 == ms2);
}
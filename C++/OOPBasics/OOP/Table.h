#pragma once

#include <iostream>

/*Class objects are matrixes.*/
template <typename T>
class Table {
	template <typename T1>
	friend std::ostream& operator<<(std::ostream&, const Table<T1>&);
	template <typename T1>
	friend std::istream& operator>>(std::istream&, Table<T1>&);

public:
	// class does not have default ctor
	Table(int, int);	// ctor with parameters
	Table(int, int, const T* const *);	// ctor with parameters
	Table(const Table<T>&);	// copy ctor
	Table<T>& operator=(const Table<T>&);	// assignment operator
	~Table();	// dtor

	int row_count() const { return m_rows; }
	int column_count() const { return m_columns; }

	T& operator()(int, int);	// [i][j]
	const T& operator()(int, int) const;

	Table<T>& operator+=(const Table<T>&);
	Table<T>& operator-=(const Table<T>&);
	Table<T>& operator*=(const Table<T>&);

private:
	void allocate_and_initialize(const T* const* = nullptr);
	void deallocate();

	void check_row_index(int) const;
	void check_column_index(int) const;
	
	void check_sum_and_diff_correct(const Table<T>&) const;
	void check_mult_correct(const Table<T>&) const;

private:
	int m_rows;
	int m_columns;
	T** m_data;
};

template <typename T>
std::ostream& operator<<(std::ostream& out, const Table<T>& object) {
	for (int i = 0; i < object.m_rows; ++i) {
		for (int j = 0; j < object.m_columns - 1; ++j) {
			out << object.m_data[i][j] << ' ';
		}
		out << object.m_data[i][object.m_columns - 1] << std::endl;
	}
	return out;
}

template <typename T>
std::istream& operator>>(std::istream& in, Table<T>& object) {
	for (int i = 0; i < object.m_rows; ++i) {
		for (int j = 0; j < object.m_columns; ++j) {
			in >> object.m_data[i][j];
		}
	}
	return in;
}

template <typename T>
Table<T>::Table(int rows, int columns)
	: m_rows(rows)
	, m_columns(columns)
	, m_data(nullptr) {
	allocate_and_initialize();
}

template <typename T>
Table<T>::Table(int rows, int columns, const T* const* data)
	: m_rows(rows)
	, m_columns(columns)
	, m_data(nullptr) {
	allocate_and_initialize(data);
}

template <typename T>
Table<T>::Table(const Table<T>& object)
	: m_rows(object.m_rows)
	, m_columns(object.m_columns)
	, m_data(nullptr) {
	allocate_and_initialize(object.m_data);
}

template <typename T>
Table<T>& Table<T>::operator=(const Table<T>& object) {
	if (this != &object) {
		deallocate();
		m_rows = object.m_rows;
		m_columns = object.m_columns;
		allocate_and_initialize(object.m_data);
	}
	return *this;
}

template <typename T>
Table<T>::~Table() {
	deallocate();
}

template <typename T>
T& Table<T>::operator()(int row_index, int column_index) {
	check_row_index(row_index);
	check_column_index(column_index);
	return m_data[row_index][column_index];
}

template <typename T>
const T& Table<T>::operator()(int row_index, int column_index) const {
	check_row_index(row_index);
	check_column_index(column_index);
	return m_data[row_index][column_index];
}

template <typename T>
Table<T>& Table<T>::operator+=(const Table<T>& object) {
	check_sum_and_diff_correct(object);
	for (int i = 0; i < m_rows; ++i) {
		for (int j = 0; j < m_columns; ++j) {
			m_data[i][j] += object.m_data[i][j];
		}
	}
	return *this;
}

template <typename T>
Table<T>& Table<T>::operator-=(const Table<T>& object) {
	check_sum_and_diff_correct(object);
	for (int i = 0; i < m_rows; ++i) {
		for (int j = 0; j < m_columns; ++j) {
			m_data[i][j] -= object.m_data[i][j];
		}
	}
	return *this;
}

template <typename T>
Table<T>& Table<T>::operator*=(const Table<T>& object) {
	check_mult_correct(object);
	int r = m_rows;
	int c = object.m_columns;
	T** tmp = new T* [r];
	for (T i = 0; i < r; ++i) {
		tmp[i] = new T[c] {};
	}
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			for (int k = 0; k < m_columns; ++k) {
				tmp[i][j] += m_data[i][k] * object.m_data[k][j];
			}
		}
	}
	deallocate();
	m_rows = r;
	m_columns = c;
	m_data = tmp;
	return *this;
}

template <typename T>
void Table<T>::allocate_and_initialize(const T* const* data) {
	m_data = new T* [m_rows];
	for (int i = 0; i < m_rows; ++i) {
		m_data[i] = new T[m_columns] {};
	}
	if (data != nullptr) {
		for (int i = 0; i < m_rows; ++i) {
			for (int j = 0; j < m_columns; ++j) {
				m_data[i][j] = data[i][j];
			}
		}
	}
}

template <typename T>
void Table<T>::deallocate() {
	for (int i = 0; i < m_rows; ++i) {
		delete[] m_data[i];
	}
	delete[] m_data;
}

template <typename T>
void Table<T>::check_row_index(int row_index) const {
	if (row_index < 0 || row_index >= m_rows) {
		throw std::exception("Row index is out of bounds.");
	}
}

template <typename T>
void Table<T>::check_column_index(int column_index) const {
	if (column_index < 0 || column_index >= m_columns) {
		throw std::exception("Column index is out of bounds.");
	}
}

template <typename T>
void Table<T>::check_sum_and_diff_correct(const Table<T>& object) const {
	if (m_rows != object.m_rows || m_columns != object.m_columns) {
		throw std::exception("Not correspondig sizes of arguments.");
	}
}

template <typename T>
void Table<T>::check_mult_correct(const Table<T>& object) const {
	if (m_columns != object.m_rows) {
		throw std::exception("Not correspondig sizes of arguments.");
	}
}

template <typename T>
Table<T> operator+(Table<T> t1, const Table<T>& t2) {
	return t1 += t2;
}

template <typename T>
Table<T> operator-(Table<T> t1, const Table<T>& t2) {
	return t1 -= t2;
}

template <typename T>
Table<T> operator*(Table<T> t1, const Table<T>& t2) {
	return t1 *= t2;
}
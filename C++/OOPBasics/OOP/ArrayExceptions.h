#pragma once

#include <exception>

class IndexOutOfBoundsException : public std::exception {
public:
	IndexOutOfBoundsException() : std::exception("Index is out of bounds.") {}
};

class IndexIsLessThan0Exception : public std::exception {
public:
	IndexIsLessThan0Exception() : std::exception("Index is less than 0.") {}
};

class ArrayIsEmptyException : public std::exception {
public:
	ArrayIsEmptyException() : std::exception("Array is empty.") {}
};
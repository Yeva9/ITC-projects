#pragma once

#include <iostream>

/*Class objects are true/false sequences with fixed size.*/
class BitVector {
	friend std::ostream& operator<<(std::ostream&, const BitVector&);
	friend std::istream& operator>>(std::istream&, BitVector&);

public:
	// this class does not have default ctor
	explicit BitVector(int);	// ctor with parameters
	BitVector(int, const bool*);	// ctor with parameters
	BitVector(const BitVector&);	// copy ctroe
	BitVector& operator=(const BitVector&);	// assignment operator
	~BitVector();	// dtor

	int size() const { return m_size; }

	BitVector& operator&=(const BitVector&);
	BitVector& operator|=(const BitVector&);
	BitVector& operator^=(const BitVector&);
	BitVector& operator<<=(int);
	BitVector& operator>>=(int);

	BitVector& operator~();

	bool& operator[](int);
	const bool& operator[](int) const;

private:
	void allocate_and_initialize(const bool* = nullptr);
	void deallocate();

	void check_index(int) const;

	void check_size_correct(const BitVector&) const;

private:
	int m_size;
	bool* m_data;
};

BitVector operator&(BitVector, const BitVector&);
BitVector operator|(BitVector, const BitVector&);
BitVector operator^(BitVector, const BitVector&);
BitVector operator<<(BitVector, int);
BitVector operator>>(BitVector, int);
#pragma once

#include <iostream>

/*Class objects are natural numeric values with no value limitation.*/
class HugeInteger {
	friend std::ostream& operator<<(std::ostream&, const HugeInteger&);
	friend std::istream& operator>>(std::istream&, HugeInteger&);

public:
	explicit HugeInteger(unsigned int = 0);	// default ctor and ctor with parameters at the same time
	HugeInteger(const char*);	// ctor with parameters
	HugeInteger(const HugeInteger&);	// copy ctor
	HugeInteger& operator=(const HugeInteger&);	// assignment operator
	~HugeInteger();	// dtor

	HugeInteger& operator+=(const HugeInteger&);
	HugeInteger& operator++();
	HugeInteger operator++(int);

	bool operator==(const HugeInteger&) const;
	bool operator<(const HugeInteger&) const;

	explicit operator unsigned int();

public:
	static int get_created_object_count() { return s_created_object_count; }

private:
	static int s_created_object_count;	// Keeps the count of HugeInteger objects created during running of program.

private:
	void allocate_and_initialize(const char*);
	void deallocate();

	void resize(int);

private:
	int m_max_length;
	int m_length;
	char* m_data;
};

HugeInteger operator+(HugeInteger, const HugeInteger&);

bool operator!=(const HugeInteger&, const HugeInteger&);
bool operator<=(const HugeInteger&, const HugeInteger&);
bool operator>(const HugeInteger&, const HugeInteger&);
bool operator>=(const HugeInteger&, const HugeInteger&);
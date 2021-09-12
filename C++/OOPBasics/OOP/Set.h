#pragma once

#include <iostream>

/*Class objects are sets with value limitation [0, 10000]*/
class Set {
	friend std::ostream& operator<<(std::ostream&, const Set&);

public:
	Set();	// default ctor
	Set(int, const int*);	// ctor with parameters
	Set(const Set&);	// copy ctor
	Set& operator=(const Set&);	// assignemt operator
	~Set();	// dtor

	bool contains(int) const;	// checks if *this contains given value
	bool is_sub_set(const Set&) const;	// checks if given Multiset object is subset for *this

	Set& operator&=(const Set&);	// intersection
	Set& operator|=(const Set&);	// union
	Set& operator-=(const Set&);	// minus

	bool operator==(const Set&) const;

private:
	void allocate_and_initialize(const bool*);
	void deallocate();

	void check_size(int) const;

private:
	static const int s_set_limit = 10001;

	int m_size;
	bool* m_data;
};

Set operator&(Set, const Set&);
Set operator|(Set, const Set&);
Set operator-(Set, const Set&);

bool operator!=(const Set&, const Set&);
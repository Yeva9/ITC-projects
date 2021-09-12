#pragma once

#include <iostream>

/*Class objects are multisets with value limitation [0, 10000]*/
class MultiSet {
	friend std::ostream& operator<<(std::ostream&, const MultiSet&);

public:
	MultiSet();	// default ctor
	MultiSet(int, const int*);	// ctor with parameters
	MultiSet(const MultiSet&);	// copy ctor
	MultiSet& operator=(const MultiSet&);	// assignment operator
	~MultiSet();	// dtor

	bool contains(int) const;	// checks if *this contains given value
	bool is_sub_set(const MultiSet&) const;	// checks if given Multiset object is subset for *this

	MultiSet& operator&=(const MultiSet&);	// intersection
	MultiSet& operator|=(const MultiSet&);	// union
	MultiSet& operator-=(const MultiSet&);	// minus

	bool operator==(const MultiSet&) const;

private:
	void allocate_and_initialize(const int*);
	void deallocate();

	void check_size(int) const;

private:
	static const int s_set_limit = 10001;

	int m_size;
	int* m_data;
};

MultiSet operator&(MultiSet, const MultiSet&);
MultiSet operator|(MultiSet, const MultiSet&);
MultiSet operator-(MultiSet, const MultiSet&);

bool operator!=(const MultiSet&, const MultiSet&);
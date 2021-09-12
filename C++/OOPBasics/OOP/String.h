#pragma once

#include <iostream>

/*Class objects are character sequences.*/
class String {
	friend std::ostream& operator<<(std::ostream&, const String&);
	friend std::istream& operator>>(std::istream&, String&);

public:
	String();	// default ctor
	explicit String(const char*);	// ctor with parameters
	String(const String&);	// copy ctor
	String& operator=(const String&);	// assignment operator
	~String();	// dtor

	int size() const { return m_size; }
	int index_of(const String&) const;

	char& operator[](int);
	const char& operator[](int) const;

	String& operator+=(const String&);	// concat

	bool operator==(const String&) const;

public:
	static int get_existing_object_count() { return s_existing_object_count; }

private:
	static int s_existing_object_count;	// keeps the count of currently existing String objects

private:
	int m_max_size;
	int m_size;
	char* m_data;
};

String operator+(String, const String&);

bool operator!=(const String&, const String&);
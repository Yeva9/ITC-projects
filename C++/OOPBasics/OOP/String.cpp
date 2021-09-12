#include "String.h"

// TODO implement
std::ostream& operator<<(std::ostream& out, const String& object) {
	return out;
}

// TODO implement
std::istream& operator>>(std::istream& in, String& object) {
	return in;
}

int String::s_existing_object_count = 0;

// TODO implement
String::String() {
	++s_existing_object_count;
}

// TODO implement
String::String(const char* data) {
	++s_existing_object_count;
}

// TODO implement
String::String(const String& object) {
	++s_existing_object_count;
}

// TODO implement
String& String::operator=(const String& object) {
	if (this != &object) {
	}
	return *this;
}

// TODO implement
String::~String() {
	--s_existing_object_count;
}

// TODO implement
int String::index_of(const String&) const {
	return -1;
}

// TODO implement
char& String::operator[](int) {
	return m_data[0];
}

// TODO implement
const char& String::operator[](int) const {
	return m_data[0];
}

// TODO implement
String& String::operator+=(const String& object) {
	return *this;
}

// TODO implement
bool String::operator==(const String& object) const {
	return true;
}

String operator+(String I1, const String& I2) {
	return I1 += I2;
}

bool operator!=(const String& I1, const String& I2) {
	return !(I1 == I2);
}
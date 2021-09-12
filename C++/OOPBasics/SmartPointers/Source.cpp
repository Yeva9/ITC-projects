#include <iostream>

#include "UniquePointer.h"
#include "SharedPointer.h"

int main() {
	// Test for UniquePointer
	try
	{
		UniquePointer<int> p1(new int(10));
		std::cout << (*p1) << std::endl;

		UniquePointer<int> p2(new int(4));
		std::cout << (*p2) << std::endl;

		p1 = p2;
		std::cout << (*p1) << std::endl;

		UniquePointer<int> p3(p1);
		std::cout << (*p3) << std::endl;
	}
	catch (const std::exception & e) {
		std::cout << e.what() << std::endl;
	}

	// Test for SharedPointer
	try {
		SharedPointer<int> p1(new int(10));
		std::cout << (*p1) << std::endl;

		SharedPointer<int> p2(new int(4));
		std::cout << (*p2) << std::endl;

		p1 = p2;
		std::cout << (*p1) << std::endl;
		std::cout << (*p2) << std::endl;

		SharedPointer<int> p3(p1);
		std::cout << (*p1) << std::endl;
		std::cout << (*p2) << std::endl;
		std::cout << (*p3) << std::endl;
	}
	catch (const std::exception & e) {
		std::cout << e.what() << std::endl;
	}

	return 0;
}
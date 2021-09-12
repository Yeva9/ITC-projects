#include "Sortings.h"

#include <iostream>

int main() {
	const int n = 11;
	int a[n] = { 3, 2, 6, 8, 0, 10, 22, 2, 11, 9, 1 };

	//Sortings::bubble_sort(a, n);
	//Sortings::insertion_sort(a, n);
	//Sortings::selection_sort(a, n);
	//Sortings::merge_sort(a, 0, n - 1);
	//Sortings::quick_sort(a, 0, n - 1);
	//Sortings::radix_sort(a, n);

	for (int element : a) {
		std::cout << element << ' ';
	}
	std::cout << std::endl;

	return 0;
}
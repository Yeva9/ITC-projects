#include "Sortings.h"

#include <algorithm>
#include <queue>

void Sortings::bubble_sort(int* array, int size) {
	for (int i = 0; i < size; ++i) {
		for (int j = i + 1; j < size; ++j) {
			if (array[i] > array[j]) {
				std::swap(array[i], array[j]);
			}
		}
	}
}

void Sortings::insertion_sort(int* array, int size) {
	for (int i = 1; i < size; ++i) {
		int tmp = array[i], j = i - 1;
		while (j >= 0 && array[j] > tmp) {
			array[j + 1] = array[j];
			--j;
		}
		array[j + 1] = tmp;
	}
}

void Sortings::selection_sort(int* array, int size) {
	for (int i = 0; i < size; ++i) {
		int min_index{ i };
		for (int j = min_index + 1; j < size; ++j) {
			if (array[j] < array[min_index]) {
				min_index = j;
			}
		}
		std::swap(array[i], array[min_index]);
	}
}

namespace {
	void merge(int* array, int first, int middle, int second) {
		const int s1{ middle - first + 1 };
		const int s2{ second - middle };
		int* first_array = new int[s1] {};
		for (int i = 0; i < s1; ++i) {
			first_array[i] = array[first + i];
		}
		int* second_array = new int[s2] {};
		for (int i = 0; i < s2; ++i) {
			second_array[i] = array[middle + i + 1];
		}

		int i{}, j{}, k{ first };
		while (i < s1 && j < s2) {
			if (first_array[i] < second_array[j]) {
				array[k++] = first_array[i++];
			}
			else {
				array[k++] = second_array[j++];
			}
		}

		while (i < s1) {
			array[k++] = first_array[i++];
		}
		while (j < s2) {
			array[k++] = second_array[j++];
		}

		delete[] first_array;
		delete[] second_array;
	}
}

void Sortings::merge_sort(int* array, int first, int second) {
	if (second > first) {
		int middle{ (first + second) / 2 };	// can be overflow
		merge_sort(array, first, middle);
		merge_sort(array, middle + 1, second);
		merge(array, first, middle, second);
	}
}

namespace {
	int partition(int* array, int first, int second) {
		int pivot{ array[second] }, i{ first - 1 };
		for (int j = first; j < second; ++j) {
			if (array[j] < pivot) {
				i++;
				std::swap(array[i], array[j]);
			}
		}
		std::swap(array[i + 1], array[second]);
		return (i + 1);
	}
}

void Sortings::quick_sort(int* array, int first, int second) {
	if (first < second) {
		int pivot = partition(array, first, second);
		quick_sort(array, first, pivot - 1);
		quick_sort(array, pivot + 1, second);
	}
}

namespace {
	int bit(int n, int k) {
		return (n >> k) & 1;
	}
}

void Sortings::radix_sort(int* array, int size) {
	const int length = sizeof(int) * 8;
	std::queue<int> Q[2];
	for (int i = 0; i < length; ++i) {
		for (int j = 0; j < size; ++j) {
			Q[bit(array[j], i)].push(array[j]);
		}
		for (int i = 0, j = 0; j < 2; ++j) {
			while (!Q[j].empty()) {
				array[i++] = Q[j].front();
				Q[j].pop();
			}
		}
	}
}
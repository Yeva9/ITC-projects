#pragma once

template <typename T>
class Queue {
public:
	Queue();
	Queue(const Queue<T>&);
	Queue<T>& operator=(const Queue<T>&);
	~Queue();

	int size() const { return m_size; }
	bool is_empty() const { return m_size == 0; }

	T& front();
	const T& front() const;

	void push(const T&);
	void pop();
	
private:
	static const int MAX_SIZE = 20;

private:
	int m_max_size;
	int m_size;
	int m_front;
	int m_end;
	int* m_data;
};

template <typename T>
Queue<T>::Queue()
	: m_max_size(MAX_SIZE)
	, m_size(0)
	, m_front(-1)
	, m_end(-1)
	, m_data(nullptr) {
	m_data = new T[m_max_size]{};
}

template <typename T>
Queue<T>::Queue(const Queue<T>& q)
	: m_max_size(q.m_max_size)
	, m_size(q.m_size)
	, m_front(-1)
	, m_end(-1)
	, m_data(nullptr) {
	m_data = new T[m_max_size]{};
	for()
}
'''
This module is intended to overload Range iterator. 
'''


class Range:
    def __init__(self, start, end):
        self._current = start
        self._stop = end
        self._first = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._current < self._stop and self._current is not None:
            result = self._current
            self._current += 1
            return result
       # print("aaa:  ", result)
        self._current = self._first


r = Range(0,3)
i = iter(r)

for j in range(0,8):
    print(next(i))  




class WithIndex:
    def __init__(self, iterable, start = 0):
        self.iterable = iterable
        self._cursor = start

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor >= len(self.iterable):
            raise StopIteration
        result = self._cursor, self.iterable[self._cursor]
        self._cursor += 1
        return result

    def __getitem__(self, item):
        return self.iterable[item]

x = [3, 5, 7, 3, 5, 2]

obj = WithIndex(x, 3)

print(obj[2])

for ind, element in WithIndex(x, 0):
    print(ind, '=>', element)


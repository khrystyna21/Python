

class Mathematician:

    def square_nums(self, squared):
        self.squared = squared
        self.squared = [s**2 for s in self.squared]
        return self.squared

    def remove_positives(self, positives):
        self.positives = positives
        self.positives = [p for p in self.positives if p < 0]
        return self.positives

    def filter_leaps(self, leaps):
        self.leaps = leaps
        self.leaps = [l for l in self.leaps if l % 4 == 0]
        return self.leaps


m = Mathematician()


assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]
assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]
assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]

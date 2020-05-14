import math


class Coordinate(object):
    """
    one coordinate is compose from x and y
    """

    def __init__(self, x, y):
        """set x and y values"""
        self.x = x
        self.y = y

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def new(self):
        print("something new")

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2

        return (x_diff_sq + y_diff_sq) ** 0.5


origin = Coordinate(0, 0)
c1 = Coordinate(1, 0)
c2 = Coordinate(0, 2)
# print(c2)
# c2.new()

# print(c1 == c2)
# print(c1 == c1)
# print(c1.distance(origin))

"""
clasa Fraction(numarator, numitor) care implementeaza :
    -__init__
    -__str__(n/n)
    -__add__: returns new Fraction
    -__sub__
    -inverse: return inversa fractiei
"""


class Fraction(object):
    def __init__(self, numarator, numitor):
        assert type(numarator) == int and type(numitor) == int, "Folositi int va rog!"
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return str(self.numarator) + "/" + str(self.numitor)

    def __add__(self, other):
        n1 = self.numarator * other.numitor + other.numarator * self.numitor
        n2 = self.numitor * other.numitor
        gcd = math.gcd(n1, n2)
        return Fraction(int(n1 / gcd), int(n2 / gcd))

    def __sub__(self, other):
        n1 = self.numarator * other.numitor - other.numarator * self.numitor
        n2 = self.numitor * other.numitor
        gcd = math.gcd(n1, n2)
        return Fraction(int(n1 / gcd), int(n2 / gcd))

    def inverse(self):
        return Fraction(self.numitor, self.numarator)


f = Fraction(1, 2)
f2 = Fraction(3, 4)
f3 = f + f2
# print(f3)
f4 = f2 - f


# print(f4)

class IntSet(object):

    def __init__(self):
        self.set = set()

    def insert(self, value):
        if value not in self.set:
            self.set.add(value)
        else:
            raise Exception("Value already in Set!")

    def remove(self, value):
        if value in self.set:
            self.set.remove(value)
        else:
            raise Exception("Value not in set!")

    def member(self, value):
        return value in self.set

    def __str__(self):
        return self.set.__str__()


s = IntSet()
print(s)
s.insert(4)
s.insert(3)
print(s)
#s.remove(2)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def scalar(self, c):
        return Point(self.x * c, self.y * c)

    def len(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'({self.x},{self.y})'


A = Point(1, 2)
B = Point(3, 3)
print(A, B)
print(A + B)
print(A - B)
print(A * B)
print(A.scalar(c=3), B.scalar(c=2))
print(A.len(), B.len())



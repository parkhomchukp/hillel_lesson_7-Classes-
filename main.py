import math
from colors import colors


class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def square(self):
        return 0


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def square(self):
        return math.pi * self.radius ** 2

    def contains(self, point):
        return ((point.x - self.x) ** 2) + ((point.y - self.y) ** 2) <= self.radius ** 2


class Rectangle(Shape):

    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.height = height
        self.width = width

    def square(self):
        return self.width * self.height


class Parallelogram(Rectangle):

    def __init__(self, x, y, height, width, angle):
        super().__init__(x, y, height, width)
        self.angle = angle

    def print_angle(self):
        print(self.angle)

    def __str__(self):
        result = super().__str__()
        return result + f'\nParallelogram: {self.width}, {self.height}, {self.angle}'

    def square(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, x, y, a, b, c, angle):
        super().__init__(x, y)
        self.a = a
        self.b = b
        self.c = c
        self.angle = angle

    def semiperimeter(self):
        return (self.a + self.b + self.c) / 2

    def square(self):
        return round(
            math.sqrt(self.semiperimeter() * (self.semiperimeter() - self.a) * (self.semiperimeter() - self.b) * (
                self.semiperimeter() - self.c)),
            3
        )


class colorizer:
    def __init__(self, colour):
        self.colour = colour

    def __enter__(self):
        print(f'\033[{colors[self.colour]}m', end='')

    def __exit__(self, exc_type, exc_value, tb):
        print(f'\033[{colors["reset"]}m', end='')
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
            return False
        return True


class frange:
    def __init__(self, start, stop=None, step=None):
        self.start = start
        self.stop = stop
        self.step = step
        if self.stop is None:
            self.stop = start + 0.0
            self.start = 0.0
        if self.step is None:
            self.step = 1.0

    def __iter__(self):
        if self.step > 0:
            i = self.start
            while i < self.stop:
                yield i
                i += self.step
        elif self.step < 0:
            i = self.start
            while i > self.stop:
                yield i
                i += self.step


# First assignment test
point = Point(1, 5)
circle = Circle(0, 0, 10)
print(f'Circle contains point: {circle.contains(point)}')

# Second assignment test
p = Parallelogram(0, 0, 5, 6, 60)
print(f'Parallelogram square: {p.square()}')

# Third assignment test
t = Triangle(0, 0, 10, 15, 8, 90)
print(f'Triangle square: {t.square()}')

# Fourth assignment test
with colorizer('red'):
    print('printed in red')

print('printed in default color')

# Fifth assignment tests
assert(list(frange(5)) == [0, 1, 2, 3, 4])
assert(list(frange(2, 5)) == [2, 3, 4])
assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
assert(list(frange(1, 5)) == [1, 2, 3, 4])
assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
assert(list(frange(0, 0)) == [])
assert(list(frange(100, 0)) == [])

print('SUCCESS!')

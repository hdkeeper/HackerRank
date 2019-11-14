class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '({},{})'.format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, n):
        return Vector(self.x * n, self.y * n)

    def asDir(self):
        if self.x == 1 and self.y == 0:
            return 'H'
        elif self.x == 0 and self.y == 1:
            return 'V'
        raise RuntimeError('Invalid dir')
    
    def copy(self):
        return Vector(self.x, self.y)


v = Vector(0, 0)
for v.y in range(5):
    for v.x in range(5):
        print(v)


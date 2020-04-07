class NVector(object):

    def __init__(self, vect):
        self.v = vect

    def __add__(self, other):
        if len(self.v) == len(other):
            self.v = list(a + b for a, b in zip(self.v, other))
            return self

    def __sub__(self, other):
        if len(self.v) == len(other):
            self.v = list(a - b for a, b in zip(self.v, other))
            return self

    def __mul__(self, other):
        if len(self.v) == len(other):
            self.v = list(a * b for a, b in zip(self.v, other))
            return self

    def __const_mul__(self, c):
        self.v = list(c * x for x in self.v)
        return self

    def __len__(self):
        return len(self.v)

    def __index__(self, num):
        List = list(self.v)
        return List[num]

    def __str__(self):
        return '{}'.format(self.v)

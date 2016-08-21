class v(object):
    def __init__(self, coor):
        try:
            if not coor:
                raise ValueError
            self.coor = tuple(coor)
            self.dim = len(coor)

        except KeyboardInterrupt:
            raise
        except ValueError:
            raise ValueError('The co-ordinates must contain values')
        except TypeError:
            raise TypeError('The co-ordinates must be an iterable')

    def __str__(self):
        return 'Vector: ' + str(self.coor)

    def __eq__(self, ov):
        return self.coor == ov.coor

    # Addition

    def plus_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x + y for x, y in zip(self.coor, ov.coor)])

    def plus_scalar(self, c):
        return v([x + c for x in self.coor])

    def __add__(self, o):
        if type(o) in [int, float]:
            return self.plus_scalar(o)
        elif type(o) is v:
            return self.plus_vector(o)
        else:
            return NotImplemented

    def __radd__(self, o):
        return self.__add__(o)

    # Subtraction

    def minus_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x + y for x, y in zip(self.coor, ov.coor)])

    def minus_scalar(self, c):
        return v([x - c for x in self.coor])

    def __sub__(self, o):
        if type(o) in [int, float]:
            return self.plus_scalar(o)
        elif type(o) is v:
            return self.plus_vector(o)
        else:
            return NotImplemented

    def __rsub__(self, o):
        return self.__sub__(o)

    # Multiplication

    def times_scalar(self, c):
        return v([c * x for x in self.coor])

    def times_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x * y for x, y in zip(self.coor, ov.coor)])

    def __mul__(self, o):
        if type(o) in [int, float]:
            return self.times_scalar(o)
        elif type(o) is v:
            return self.times_vector(o)
        else:
            return NotImplemented

    def __rmul__(self, o):
        return self.__mul__(o)

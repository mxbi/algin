from math import floor, sqrt

class v(object):
    def __init__(self, coor):
        try:
            if not coor:
                raise ValueError
            if type(coor) is v:
                self.coor = coor.coor
            else:
                self.coor = list(coor)
            self.dim = len(self.coor)

        except KeyboardInterrupt:
            raise
        except ValueError:
            raise ValueError('The co-ordinates must contain values')
        except TypeError:
            raise TypeError('The input type ' + str(type(coor)) + ' is not supported.')

    # Called when converting to string or printing
    def __str__(self):
        return 'Vector: ' + str(self.coor)

    def __repr__(self):
        return self.__str__()

    # Checking for equality
    def __eq__(self, ov):
        return self.coor == ov.coor

    # Allow for conversions to lists etc
    def __iter__(self):
        return iter(self.coor)

    # Allow for dimension selection
    def __getitem__(self, i):
        return self.coor[i]

    ## Addition

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

    ## Subtraction

    def minus_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x - y for x, y in zip(self.coor, ov.coor)])

    def minus_scalar(self, c):
        return v([x - c for x in self.coor])

    def rminus_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([y - x for x, y in zip(self.coor, ov.coor)])

    def rminus_scalar(self, c):
        return v([c - x for x in self.coor])

    def __sub__(self, o):
        if type(o) in [int, float]:
            return self.minus_scalar(o)
        elif type(o) is v:
            return self.minus_vector(o)
        else:
            return NotImplemented

    def __rsub__(self, o):
        if type(o) in [int, float]:
            return self.rminus_scalar(o)
        elif type(o) is v:
            return self.rminus_vector(o)
        else:
            return NotImplemented

    ## Multiplication

    def times_scalar(self, c):
        return v([x * c for x in self.coor])

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

    ## True divison

    def truediv_scalar(self, c):
        return v([x / c for x in self.coor])

    def truediv_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x / y for x, y in zip(self.coor, ov.coor)])

    def __truediv__(self, o):
        if type(o) in [int, float]:
            return self.truediv_scalar(o)
        elif type(o) is v:
            return self.truediv_vector(o)
        else:
            return NotImplemented

    def rtruediv_scalar(self, c):
        return v([c / x for x in self.coor])

    def rtruediv_vector(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([y / x for x, y in zip(self.coor, ov.coor)])

    def __rtruediv__(self, o):
        if type(o) in [int, float]:
            return self.rtruediv_scalar(o)
        elif type(o) is v:
            return self.rtruediv_vector(o)
        else:
            return NotImplemented

    ## Floor division

    def __floordiv__(self, o):
        if type(o) in [int, float, v]:
            return v([floor(x) for x in self.__truediv__(o).coor])
        else:
            return NotImplemented

    def __rfloordiv__(self, o):
        if type(o) in [int, float, v]:
            return v([floor(x) for x in self.__rtruediv__(o).coor])

    # Magnitude of vector
    def mag(self):
        return sqrt(sum([x ** 2 for x in self.coor]))

    # Normalised vector
    def norm(self):
        return v(self / self.mag())

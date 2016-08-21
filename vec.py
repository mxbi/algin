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

    def plus(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x + y for x, y in zip(self.coor, ov.coor)])

    def __add__(self, ov):
        return self.plus(ov)

    def minus(self, ov):
        assert self.dim == ov.dim, 'Vectors must be the same dimensionality.'
        return v([x + y for x, y in zip(self.coor, ov.coor)])

    def __sub__(self, ov):
        return self.minus(ov)

    def times_scalar(self, c):
        return v([c * x for x in self.coor])

    def __mul__(self, o):
        if type(o) in [int, float]:
            return self.times_scalar(o)
        else:
            raise TypeError('Vectors can only be multiplied by a number.')

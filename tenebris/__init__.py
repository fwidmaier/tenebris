def operator(f):
    def wrapper(self, other):
        if isinstance(other, Dual):
            return f(self, other)
        return f(self, Dual(other))

    return wrapper


class Dual:
    """
    A small class that implements the basic arithmetic of dual numbers.
    """

    def __init__(self, a, b=0):
        self.a = a
        self.b = b

    def __repr__(self):
        return str(self)

    def __str__(self):
        if self.b == 0:
            return str(self.a)
        return f"{self.a} + {self.b}ε"

    def __neg__(self):
        return Dual(-1 * self.a, -1 * self.b)

    def __pos__(self):
        return self

    @operator
    def __add__(self, other):
        return Dual(self.a + other.a, self.b + other.b)

    @operator
    def __radd__(self, other):
        return other + self

    @operator
    def __sub__(self, other):
        return Dual(self.a - other.a, self.b - other.b)

    @operator
    def __rsub__(self, other):
        return other - self

    @operator
    def __mul__(self, other):
        return Dual(self.a * other.a, self.a * other.b + self.b * other.a)

    @operator
    def __rmul__(self, other):
        return other * self

    @operator
    def __truediv__(self, other):
        if other.a == 0:
            raise ZeroDivisionError
        return Dual(self.a / other.a, (self.b * other.a - self.a * other.b) / (other.a * other.a))

    @operator
    def __rtruediv__(self, other):
        return other / self


# TODO: make this definition of d a bit more readable
d = lambda f, n=1: d(d(f), n - 1) if n > 1 else lambda x: (lambda t: t.b if isinstance(t, Dual) else 0)(f(Dual(x, 1)))

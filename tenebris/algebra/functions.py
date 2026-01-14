from tenebris.algebra.expressions import Expression
from tenebris.algebra.operations import Constant
from tenebris.solver import solve


class FunctionCall(Expression):
    def __init__(self, name, expression, func=None):
        super().__init__()
        self.name = name
        self.expression = expression
        self.func = func

    def __str__(self):
        if isinstance(self.expression, Constant):
            return f"{self.name}({str(self.expression)})"
        return self.name + f"{str(self.expression)}"

    def __copy__(self):
        return FunctionCall(self.name, self.expression, func=self.func)

    def __call__(self, **kwargs):
        term_eval = self.expression(**kwargs)

        if self.func is not None:
            kwargs[self.name] = self.func

        if self.name in list(kwargs) and not isinstance(term_eval, Expression):
            return kwargs[self.name](self.expression(**kwargs))

        copy = self.__copy__()
        copy.term = copy.term(**kwargs)
        if not isinstance(copy.term, Expression):
            copy.term = Constant(copy.term)
        return copy

    def __contains__(self, item):
        """
        Just for playing around...
        """
        assert not isinstance(item, Expression)  # TODO: this can also be symbolic...
        assert self.func is not None
        inv = lambda t: solve(self.func, t, 0)
        try:
            i = inv(item).a
            return i in self.expression
        except Exception as e:
            raise e


class SymbolicFunction:
    def __init__(self, name="f", val=None):
        self.name = name
        self.val = val

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def __call__(self, term: Expression):
        return FunctionCall(self.name, term, func=self.val)


def symbolic(name):  # TODO: use functools for the decorator...
    def decorator(func):
        def wrapper(term):
            if isinstance(term, Expression):
                return FunctionCall(name, term, func=func)
            return func(term)
        return wrapper
    return decorator

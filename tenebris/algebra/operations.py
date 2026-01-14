from typing import override

from tenebris.algebra.expressions import Expression
from abc import ABC, abstractmethod


class Constant(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def __str__(self):
        return str(self.value)

    def __call__(self, **kwargs):
        return self.value


class Operation(Expression, ABC):
    def __init__(self, sym, operation, *expressions):
        super().__init__()
        self.sym = sym
        self.operation = operation
        self.expressions = self.fold_constants(*expressions)

    @classmethod
    @abstractmethod
    def new(cls, *expressions):
        return cls(*expressions)

    def fold_constants(self, *expressions):
        if all(isinstance(term, Constant) for term in expressions):
            c = expressions[0].value
            for term in expressions[1:]:
                c = self.operation(c, term.value)
            return [Constant(c)]
        return expressions

    def __str__(self):
        return f"({self.sym.join(list(map(str, self.expressions)))})"

    def __call__(self, **kwargs):
        if len(self.expressions) == 1:
            return self.operation(self.expressions[0](**kwargs))

        result = self.operation(self.expressions[0](**kwargs), self.expressions[1](**kwargs))
        for expression in self.expressions[2:]:
            result = self.operation(result, expression(**kwargs))

        return result


class UnaryOperation(Operation, ABC):
    def __init__(self, sym, operation, expression):
        super().__init__(sym, operation, expression)

    def __str__(self):
        return f"{self.sym}{str(self.expressions[0])}"

    @classmethod
    def new(cls, expression):
        return super().new(expression)


class Associative(Operation, ABC):
    def __init__(self, sym, operation, *expressions):
        super().__init__(sym, operation, *expressions)

    @classmethod
    def flatten_terms(cls, *expressions):
        same_operation = list()
        for expression in expressions:
            if isinstance(expression, cls):
                same_operation += expression.expressions
            else:
                same_operation.append(expression)

        return same_operation

    @classmethod
    def new(cls, *expressions):
        return super().new(*cls.flatten_terms(*expressions))


class Commutative(Operation, ABC):
    def __init__(self, sym, operation, *expressions):
        super().__init__(sym, operation, *expressions)

    @override
    def fold_constants(self, *expressions):
        tt = list()
        c = None
        for term in expressions:
            if isinstance(term, Constant):
                if c is None:
                    c = term.value
                else:
                    c = self.operation(c, term.value)
            else:
                tt.append(term)
        return [Constant(c)] + tt if c is not None else tt

    @classmethod
    def new(cls, *expressions):
        return super().new(*expressions)

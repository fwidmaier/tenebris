from abc import ABC, abstractmethod
from collections.abc import Set as AbstractPySet

from tenebris.algebra.expressions import Expression
from tenebris.algebra.operations import Associative, Commutative, UnaryOperation


def set_operator(func):
    def wrapper(self, other):
        if isinstance(other, AbstractPySet):
            other = FiniteSet(*other)
        return func(self, other)
    return wrapper


class AbstractSet(Expression, ABC):
    @abstractmethod
    def __contains__(self, item):
        pass

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Sets are not callable.")

    def __neg__(self):
        return Complement.new(self)

    @set_operator
    def __and__(self, other):
        return Intersection.new(self, other)

    @set_operator
    def __or__(self, other):
        return Union.new(self, other)

    @set_operator
    def __sub__(self, other):
        return Intersection.new(self, -other)

    @set_operator
    def times(self, other):
        return CrossProduct.new(self, other)


class Complement(UnaryOperation, AbstractSet):
    def __init__(self, s):
        super().__init__("~", None, s)

    def __contains__(self, item):
        return item not in self.expressions[0]


class Intersection(Associative, Commutative, AbstractSet):
    def __init__(self, *sets):
        super().__init__("∩", None, *sets)

    def __contains__(self, item):
        return all(item in s for s in self.expressions)


class Union(Associative, Commutative, AbstractSet):
    def __init__(self, *sets):
        super().__init__("∪", None, *sets)

    def __contains__(self, item):
        return any(item in s for s in self.expressions)


class CrossProduct(Associative, AbstractSet):
    def __init__(self, *sets):
        super().__init__("×", None, *sets)

    def __contains__(self, item):
        if len(item) != len(self.expressions):
            return False
        return all(item[i] in self.expressions[i] for i in range(len(self.expressions)))


class FiniteSet(AbstractSet):
    def __init__(self, *elements):
        super().__init__()
        self.elements = frozenset(elements)

    def __str__(self):
        return "{" + f"{', '.join(list(map(str, self.elements)))}" + "}"

    def __contains__(self, item):
        return item in self.elements


class QualifiedSet(AbstractSet):
    def __init__(self, predicate, name="Q"):  # TODO: better naming of these sets
        super().__init__()
        self.predicate = predicate
        self.name = name

    def __str__(self):
        return self.name

    def __contains__(self, item):
        if isinstance(item, tuple):
            if len(item) == 1:
                item = item[0]
        return self.predicate(item)


EmptySet = QualifiedSet(lambda x: False, "∅")

from abc import ABC, abstractmethod

from tenebris.algebra.expressions import Expression
from tenebris.algebra.operations import Associative, Commutative


class Set(Expression, ABC):
    @abstractmethod
    def __contains__(self, item):
        pass

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Sets are not callable.")

    def __and__(self, other):
        return Intersection.new(self, other)

    def __or__(self, other):
        return Union.new(self, other)

    def times(self, other):
        return CrossProduct.new(self, other)


class Intersection(Associative, Commutative, Set):
    def __init__(self, *sets):
        super().__init__("∩", None, *sets)

    def __contains__(self, item):
        return all(item in s for s in self.expressions)


class Union(Associative, Commutative, Set):
    def __init__(self, *sets):
        super().__init__("∪", None, *sets)

    def __contains__(self, item):
        return any(item in s for s in self.expressions)


class CrossProduct(Associative, Set):
    def __init__(self, *sets):
        super().__init__("×", None, *sets)

    def __contains__(self, item):
        assert len(item) == len(self.expressions)
        return all(item[i] in self.expressions[i] for i in range(len(self.expressions)))


from abc import ABC, abstractmethod

from tenebris.algebra.expressions import Expression
from tenebris.algebra.operations import Associative, Commutative


class AbstractSet(Expression, ABC):
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


class Set(AbstractSet):
    def __init__(self, *elements):
        self.elements = list(set(elements))

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
        return self.predicate(item)
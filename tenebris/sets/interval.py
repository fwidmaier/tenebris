from tenebris.sets import Set


class Interval(Set):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def __str__(self):
        return f"[{self.a}, {self.b}]"

    def __contains__(self, item):
        return self.a <= item <= self.b

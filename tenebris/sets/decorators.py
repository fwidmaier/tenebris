from tenebris.sets import AbstractSet


def domain(d: AbstractSet):
    def decorator(func):
        def wrapper(x):
            assert x in d
            return func(x)
        return wrapper
    return decorator

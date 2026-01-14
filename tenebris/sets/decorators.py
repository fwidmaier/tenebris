from tenebris.sets import AbstractSet


def domain(d: AbstractSet):
    def decorator(func):
        def wrapper(*args):
            assert args in d
            return func(*args)
        return wrapper
    return decorator

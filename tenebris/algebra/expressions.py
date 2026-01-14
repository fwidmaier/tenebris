from abc import ABC, abstractmethod


class Expression(ABC):
    def __new__(cls, *args, **kwargs):
        print(cls)
        return super().__new__(cls)

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __call__(self, **kwargs):
        pass

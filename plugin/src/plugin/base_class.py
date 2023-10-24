import sys
from abc import ABC, abstractmethod


class AbstractClass(ABC):

    concrete_classes: dict = {}

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    @staticmethod
    def instance(class_name):
        return AbstractClass.concrete_classes[class_name]()


def register_concrete_class(cls):
    AbstractClass.concrete_classes[cls.__name__] = cls
    return cls


__all__ = [
    "AbstractClass",
    "register_concrete_class",
]

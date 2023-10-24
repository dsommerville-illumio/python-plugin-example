from .base_class import *


@register_concrete_class
class ConcreteClass1(AbstractClass):

    def operation1(self):
        print("Plugin 1: Concrete 1 Operation 1")

    def operation2(self):
        print("Plugin 1: Concrete 1 Operation 2")


__all__ = [ "ConcreteClass1" ]

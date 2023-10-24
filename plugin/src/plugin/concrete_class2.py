from .base_class import *


@register_concrete_class
class ConcreteClass2(AbstractClass):

    def operation1(self):
        print("Plugin 1: Concrete 2 Operation 1")

    def operation2(self):
        print("Plugin 1: Concrete 2 Operation 2")


__all__ = [ "ConcreteClass2" ]

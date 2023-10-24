try:
    from plugin import AbstractClass, register_concrete_class


    @register_concrete_class
    class PluginExtension(AbstractClass):
        def operation1(self):
            print("My plugin: Extended operation 1")

        def operation2(self):
            print("My plugin: Extended operation 2")
except ImportError:
    print("Failed to import plugin base class")

# Protocol vs ABC
Protocols fascilitate the interface segregation principle, one of the core OOP SOLID principles. Protocols provide support for structural subtyping (i.e. structural matching/ duck typing), whereas abstract base classes support nominal subtyping (i.e. subtypes must be declared explicitly through inheritance). Protocols will not throw an error at runtime until a method is used which isn't  implemented as expected, i.e. type checking will catch errors, but no error is raised at runtime. Abstract base classes define how a class should be created, and will therefore throw an error at runtime when the object is instantiated if the class has not been implemented correctly.

## Abstract base classes example
Try commenting out an abstract method in device.py. Then comment out a method in devices.py.You should see by the linting (use "python.analysis.typeCheckingMode": "basic" to see it linted in VSCode settings) that you won't be able to create an object if it doesn't implement all methods in the abstract base class.

If you wanted to separate out the methods into different interfaces, you'd have to go down a multiple inheritance route.

## Protocol example
Protocols provide flexibility to work with legacy code, allow interfaces to be defined where they are needed, and avoid multiple inheritance, which is always a good thing.

Try commenting out the get_status_update implementation in devices to see that the error is found by linting only where the object is used as an expected interface, and not upon creation. If you use protocols you might want to use them with a static type checker such as mypy.

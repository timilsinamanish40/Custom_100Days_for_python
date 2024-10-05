# Class decorator to add logging behavior
def class_logger(cls):
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            print(f"Creating instance of {cls.__name__}")
            super().__init__(*args, **kwargs)

        def __getattribute__(self, name):
            attr = super().__getattribute__(name)
            if callable(attr):
                def new_func(*args, **kwargs):
                    print(f"Calling method {name} with arguments: {args} {kwargs}")
                    result = attr(*args, **kwargs)
                    print(f"Method {name} returned: {result}")
                    return result
                return new_func
            return attr
    return Wrapper

# A simple class that will be decorated
@class_logger
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Using the class
calc = Calculator()
calc.add(10, 5)
calc.subtract(10, 5)

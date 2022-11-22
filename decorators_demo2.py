"""
    This is part two on decorators. Essentially, the previous module
    was illustrative. This module accomplishes the exact same thing with the
    correct decorator syntax.
"""


def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this before {original_function.__name__}()')
        return original_function()
    return wrapper_function


@decorator_function
def display():
    print('display() function ran')

print(display)
display()

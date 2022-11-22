"""
The main application for a decorator function is to apply a certain
    set of functionality (defined in the decorator function), to
    any other function that gets decorated with it.
    To Decorate = To add things on to an object.
A decorator allows us to maintain added functionality (such as logging)
    in one location and easily apply it anywhere we want and to any other
    functions in the codebase.
What is a main application of a decorator function?
    The example in the Corey Schafter tutorial is that of a logging decorator
    that writes a file with details of the other functions being ran and what
    arguments were passed to those function. Imagine you want to know the detail
    about every time a decorated function is ran. The wrapper function could
    open a text file and adds that the decorated function was run and also the
    arguments it was run with.
    Another common usage of a decorator is to monitor or time how long it takes
    for a function to run.
A decorator is a function that takes another function as an argument,
    add some kind of functionality, and then returns another function
    without altering the source code of the original function that was
    decorated.
Why do we want to use decorator functions?
    Using decorator functions allows to easily add functionality to our
    existing functions by decorating additional functionality inside of our wrapper.
    In the example below, we can add functionality to the display() function
    without modifying it. We can add new functionality to the display()
    function by simply adding new functionality to the wrapper function.
"""

# # Here was the example from the closures_demo.py module
# def outer_function(msg):
#     def inner_function(msg):
#         print(msg)
#     return inner_function

# Simplest form of a decorator. Passes in a function, returns the original
#   function as the instance.
def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed this line before {original_function.__name__}()')
        return original_function()
    return wrapper_function


def display():
    print('display() function ran')


# "Decorate" the display function by making it an instance of the
#   wrapper function as you can see when you print it.
decorated_display_instance = decorator_function(display)
print(decorated_display_instance)

# Invoke the decorated display function. This invokes the 
#   wrapper function which invokes the original function
#   and returns it.
decorated_display_instance()

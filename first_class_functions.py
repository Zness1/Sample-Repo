"""
    Functions are objects too. And as such they can 
    be passed into other functions (higher order functions)
    such as the 'map' function. In the case below, the 
    square and cube functions are passed as arguments to the
    my_map function. The square and cube functions are then
    executed inside my_map along with the list argument.
    """


# def square(x):
#     "Squares a number"
#     return x*x


# def cube(x):
#     "Cubes a number"
#     return x*x*x


# def my_map(func, arg_list):
#     "Executes a function with the given list"
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result


# squares = my_map(square, [1, 2, 3, 4, 5])
# cubes = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)
# print(cubes)

# The below example is an example of a 'Closure'
def logger(msg):
    "Docstring"
    def log_message():
        "Docstring"
        print('Log: ', msg)

    return log_message


instance_variable = logger('Hi')
instance_variable()

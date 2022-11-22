"""
A Closure is an inner function that remembers and has access to
variables in the local scope in which it was created, even after
the outer function has finished executing.
A Closure 'closes-over' the free variables from their environment.
"""

# In this case the 'free variable' is 'msg' passed to the outer function
def outer_func(msg):
    "Docstring"
    message = msg

    # The free variable is then closed in the inner function
    def inner_func():
        print(message)

    # Note there are no parenthesis, we are not invoking the inner function
    #   we are returning the inner function itelf to the instance variable
    #   with the now-closed free variable 'msg'
    return inner_func

# Each of these functions is now equal to the inner function and waiting to
#   be executed
hi_func = outer_func('Hi')
hello_func = outer_func('Hello')

# Here you can see that hi_func & hello_func instances are function objects
#   of inner_func that were returned when outer_func was invoked.
print(hi_func)
print(hello_func)

# Here you can see that when the function instances are executed they
# 'remember' the closed variables that were passed to them even though
# the outer function is not being called.
hi_func()
hello_func()

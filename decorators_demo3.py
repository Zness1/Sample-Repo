"""
Here we created a decorator function that times and prints the execution
time of any function that is passed into it.
"""

# Decorator unction
def my_timer(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original_function.__name__} ran in: {t2} seconds.')
        return result

    return wrapper


# Decorated function. This function is "decorated" with my_timer()
@my_timer
def display_info(name, age):
    import time
    print(f'display_info() ran with arguments ({name}, {age})')
    time.sleep(1)

display_info('Hank', 30)

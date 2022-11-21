"""Converting functions into generators"""
# A generator is a type of function,
#   but instead of returning a value or object it 'yields' values one at a time
#   without having to store the return value in memory.
# To convert a function to a generator, use the keyword 'yield' instead of 'return'.
# A list holds all the values in memory.
# A generator will return the next item and
#   experience performance enhancements with large amounts of data.
# A generator is useful for extreme performance enhancement with large datak
# A generator is an 'iterator' function that performs an action 1 at a time
#   without having to pull in an entire database, dataset, list or dictionary.


def square_numbers(nums):
    """Function that takes a list and returns a list of the squares"""
    result = []
    for i in nums:
        result.append(i*i)
    return result # result keyword returns entire list


def square_numbers2(nums):
    """Function that takes a list and returns a list of squares using a generator"""
    # Generator objects to hold the result in memory, the produce the result one at a time.

    for i in nums:
        # The yield keyword converts this function to a generator,
        #   and returns one item at a time (the next item).
        yield i*i


my_nums = square_numbers([1, 2, 3, 4, 5])
print(my_nums)

my_nums2 = square_numbers2([1, 2, 3, 4, 5])
print(square_numbers) # Prints a function object
print(my_nums2)  # Prints a generator object, not the result
# print(next(my_nums2))  # next() returns the next number that is 'yielded'
# print(next(my_nums2))
# print(next(my_nums2))
# print(next(my_nums2))
# print(next(my_nums2))
# print(next(my_nums2)) Throws a StopIteration exception because the generator is 'exhausted'


# Using a for loop with a generator because the for loop 'knows' to stop at the end of a generator
for num in my_nums2:
    print(num)

# A generator as a list comprehension, use parentesis to create a generator
my_nums3 = (x*x for x in [1, 2, 3, 4, 5])
print(my_nums3)
for num in my_nums3:
    print(num)

# A generator as a list comprehension, with an output as list
# Converting generators to a list like this defeats the purpose of performance enhancement
my_nums4 = (x*x for x in [1, 2, 3, 4, 5])
print(list(my_nums4))

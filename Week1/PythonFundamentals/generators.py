### generator should be used when you are working with a data structure to store values 
# and don't want the data structure to fill up the memory because of the size of it.

# to perform a single function/operation on a set of inputs, you can use generator to use it as an iterable
# which only gives you the output when you ask for it. 



# creates an iterable object which executes completely when the function is called to store the values
# this function will store all the n values at once when the function is called 
# doesn't matter if the value is necessary or will be used or not.
def squares(n):
    return [i**2 for i in range(1, n+1)]

# creates a generator object which only stores the value in an iterable when it is called
# this will only give you the value when you ask for it, saving memory which would have been wasted if all the inputs
# were processed and stored in a data structure.
def generate_squares(n):
    for i in range(1, n+1):
        yield i**2

result1 = squares(5)
print("List iterable: ", result1)

# 1 way to print generators, automatically calls __next__()
for i in generate_squares(5):
    print("Generator iterable using for loop: ", i)
print("-" * 15)
# 2nd way to print values from a generator, manually calling __next__()
result2 = generate_squares(5)
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))
print(next(result2))

print("-" * 15)

sq = (i**2 for i in range(1, 6))
for i in sq:
    print(i)

'''
#~> Notes 
    #? itertools.product is implemented at c level and said to be faster than nested for loops in python for larger iterations
    #? In below code, it is always nested loops faster than  itertools.product
    
    #? Explore itertools module in python for other such implementations - https://docs.python.org/3/library/itertools.html
'''

# Way-1
"""
import itertools
import time

# Number of iterations
N = 30000

# Nested for loops
start_time = time.time()

for i in range(N):
    for j in range(N):
        pass

end_time = time.time()
nested_loops_time = end_time - start_time

# itertools.product()
start_time = time.time()

for _ in itertools.product(range(N), range(N)):
    pass

end_time = time.time()
itertools_product_time = end_time - start_time

print("Nested for loops time:", nested_loops_time)
print("itertools.product() time:", itertools_product_time)

"""

# Way-2
import itertools
import timeit

N = 30000

# Nested for loops
nested_loops_time = timeit.timeit(
    '''
for i in range(10000):
    for j in range(10000):
        pass
    ''',
    number=10
)

# itertools.product()
itertools_product_time = timeit.timeit(
    '''
import itertools
for _ in itertools.product(range(10000), range(10000)):
    pass
    ''',
    number=10
)

print("Nested for loops time:", nested_loops_time)
print("itertools.product() time:", itertools_product_time)

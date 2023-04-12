'''
#% -> fronzenset is faster and memory efficient than set
#%    Reason: frozenset is immutable and hence requires fix size hashtable and less metadata to maintain the immutability

#% -> Set requires the more metadata to maintain the mutability
'''

#? Unique unordered collection of items
#? Immutable like tuple, hence can be used as dictionary key
frozen_st = frozenset([1,2,3,3])    #? Can be created from the iterable
print(frozen_st)

print("\n set and frozenset comparision")
st = set(range(100000))
fst = frozenset(range(100000))

import sys

print("     size of set : ", sys.getsizeof(st))
print("     size of fronzenset : ", sys.getsizeof(fst))

import random
import string
import sys
import time

# Generate a list of 1 million random strings
my_list = [''.join(random.choices(string.ascii_lowercase, k=10)) for _ in range(1000000)]

# Create a set and measure its size
start_time = time.time()
my_set = set(my_list)
set_size = sys.getsizeof(my_set)
print("Size of set:", set_size)
end_time = time.time()
print("Time taken to create set:", end_time - start_time, "seconds")

# Create a frozenset and measure its size
start_time = time.time()
my_frozenset = frozenset(my_list)
frozenset_size = sys.getsizeof(my_frozenset)
print("Size of frozenset:", frozenset_size)
end_time = time.time()
print("Time taken to create frozenset:", end_time - start_time, "seconds")


from memory_profiler import profile
from pympler import asizeof
import sys

n = 1000000

@profile
def set_vs_frozenset():
    s = set([ i for i in range(n)])  # set
    fs = frozenset([ i for i in range(n)])  # frozenset

    set_size = s.__sizeof__()
    frozenset_size = fs.__sizeof__()
    
    print("asizeof : Set : ", asizeof.asizeof(s))
    print("asizeof : FrozenSet : ", asizeof.asizeof(fs))
    
    print("normal : Set : ", sys.getsizeof(s))
    print("normal : FrozenSet : ", sys.getsizeof(fs))

    size_diff = frozenset_size - set_size
    percent_diff = (size_diff / set_size) * 100

    print(f'set size: {set_size} bytes')
    print(f'frozenset size: {frozenset_size} bytes')
    print(f'size difference: {size_diff} bytes ({percent_diff:.2f}% difference)')

if __name__ == '__main__':
    set_vs_frozenset()

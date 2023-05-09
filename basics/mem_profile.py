from memory_profiler import profile

@profile
def set_vs_frozenset():
    s = {1, 2, 3, 4, 5}  # set
    fs = frozenset({1, 2, 3, 4, 5})  # frozenset

    set_size = s.__sizeof__()
    frozenset_size = fs.__sizeof__()

    size_diff = frozenset_size - set_size
    percent_diff = (size_diff / set_size) * 100

    print(f'set size: {set_size} bytes')
    print(f'frozenset size: {frozenset_size} bytes')
    print(f'size difference: {size_diff} bytes ({percent_diff:.2f}% difference)')

if __name__ == '__main__':
    set_vs_frozenset()

def quicksort(arr: list[int]) -> list[int]:
    """
    This implementation is with an open loop, the ergonomic is 
    using an list comprehension.
    >>> quicksort([3, 2, 1])
    [1, 2, 3]
    >>> quicksort([30, 10, 15, 7])
    [7, 10, 15, 30]
    >>> quicksort([9, 2])
    [2, 9]
    >>> quicksort([9])
    [9]
    >>> quicksort([])
    []
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    greater = []
    less = []
    for i in arr[1:]:
        if i <= pivot:
            less.append(i)
            continue
        greater.append(i)
    return quicksort(less) + [pivot] + quicksort(greater)

def quicksort_2(arr: list[int]) -> list[int]:
    """
    >>> quicksort_2([3, 2, 1])
    [1, 2, 3]
    >>> quicksort_2([30, 10, 15, 7])
    [7, 10, 15, 30]
    >>> quicksort_2([9, 2])
    [2, 9]
    >>> quicksort_2([9])
    [9]
    >>> quicksort_2([])
    []
    """
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    greater = [i for i in arr[1:] if i > pivot]
    less = [i for i in arr[1:] if i <= pivot]
    return quicksort_2(less) + [pivot] + quicksort_2(greater)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
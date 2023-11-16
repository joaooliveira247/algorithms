def sum(arr: list[int]) -> int:
    """
    >>> sum([1, 2, 3])
    6
    """
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

def len(arr: list[int]) -> int:
    """
    >>> len([1, 2, 3, 4, 5])
    5
    >>> len([])
    0
    >>> len([1])
    1
    """
    if arr == []:
        return 0
    return 1 + len(arr[1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
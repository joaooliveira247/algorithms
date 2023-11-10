def sum_natural_numbers(n: int) -> int:
    """
    >>> sum_natural_numbers(3)
    6
    """
    if n < 0:
        raise ValueError("'n' need be greater than 0.")
    if n <= 1:
        return n
    return n + sum_natural_numbers(n - 1)


def sum_array_elements(arr: list[int]) -> int:
    """
    >>> sum_array_elements([1, 2, 3, 4, 5, 6])
    21
    """
    if len(arr) <= 0:
        return 0
    return arr[0] + sum_array_elements(arr[1:])


def factorial(n: int) -> int:
    """
    >>> factorial(6)
    720
    """
    if n == 1:
        return n
    return n * factorial(n - 1)
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()

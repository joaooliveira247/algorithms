def find_smallest(arr: list[int]) -> int:
    """
    Find the smallest index of a value in a list of integers.

    # Example

    a = find_smallest([9, 18, 7, 6, 33, 2])

    print(a)

    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr: list[int]) -> list[int]:
    """
    Sort a list of integers.

    # Example
    a = [32, 17, 54, 88, 49, 2, 99, 3]

    b = selection_sort(a)

    print(b)

    """
    new_arr: list[int] = []
    for _ in range(len(arr)):
        smallest: int = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


def main() -> None:
    print(selection_sort([32, 17, 54, 88, 49, 2, 99, 3]))


if __name__ == "__main__":
    main()

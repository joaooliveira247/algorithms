def binary_search(arr: list[int], item: int) -> int | None:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        low = mid + 1
    return None


def main() -> None:
    arr = [1, 2, 3, 8, 9, 17]
    print(binary_search(arr, 3))


if __name__ == "__main__":
    main()

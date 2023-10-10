package main

import (
	"fmt"
)

func binary_search(arr []int, item int) (int, bool) {
	low := 0
	high := len(arr) - 1

	for low <= high {
		mid := (low + high) / 2
		guess := arr[mid]
		if guess == item {
			return mid, true
		}
		if guess > item {
			high = mid - 1
		} else {
			low = mid + 1
		}
	}
	return 0, false
}

func main() {
	arr := []int{1, 3, 5, 7, 9, 17, 28}
	fmt.Println(binary_search(arr, 17))
}

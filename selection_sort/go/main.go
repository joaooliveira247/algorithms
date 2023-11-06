package main

import(
	"fmt"
)

func pop[T interface{}](arr []T, index int) ([]T, T) {
	// Remove and return item at index (default last).

	// Raises IndexError if list is empty or index is out of range
	value := arr[index]
	return append(arr[:index], arr[index+1:]...), value
}

func findSmallest(arr []int) int {
	smallestIndex := 0
	smallest := arr[smallestIndex]
	for i := 1; i < len(arr); i++ {
		if arr[i] < smallest {
			smallest = arr[i]
			smallestIndex = i
		}
	}
	return smallestIndex
}

func selectionSort(arr []int) []int {
	newArr := []int{}
	for range arr {
		p := 0
		smallest := findSmallest(arr)
		arr, p = pop(arr, smallest)
		newArr = append(newArr, p)
	}

	return newArr
}

func main() {
	newArr := []int{7, 5, 3, 18, 12}
	fmt.Println(selectionSort(newArr))
}

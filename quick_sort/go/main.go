package main

func quickSort(arr []int) []int {
	if len(arr) < 2 {
		return arr
	}
	pivot := arr[0]
	greater := []int{}
	less := []int{}
	for _, v := range arr[1:] {
		if v > pivot {
			greater = append(greater, v)
			continue
		}
		less = append(less, v)
	}
	return append(append(quickSort(less), pivot), quickSort(greater)...)
}

package main

func SumNaturalNumbers(n uint) uint {
	if n < 1 {
		return n
	}
	return n + SumNaturalNumbers(n - 1)
}

func SumArrayElements(arr []int) int {
	if len(arr) == 0 {
		return 0
	}
	return arr[0] + SumArrayElements(arr[1:])
}

func Factorial(n uint) uint {
	if n < 1 {
		return 1
	}
	return n * Factorial(n - 1)
		
}
package main

import "testing"

func TestSumNaturalNumbers(t *testing.T) {
	result := SumNaturalNumbers(3)
	if result != 6 {
		t.Errorf("Expect 6 got %d", result)
	}
}

func TestSumArrayElements(t *testing.T) {
	result := SumArrayElements([]int{1, 2, 3, 4, 5, 6,})
	if result != 21 {
		t.Errorf("Expect 21 got %d", result)
	}
}

func TestFactorial(t *testing.T) {
	result := Factorial(6)
	if result != 720 {
		t.Errorf("Expect 720 got %d", result)
	}
}
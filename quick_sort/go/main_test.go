package main

import (
	"testing"
	"reflect"
)

func TestQuickSort(t *testing.T) {
	result := quickSort([]int{3, 2, 1})
	expect := []int{1, 2, 3}
	if !reflect.DeepEqual(result, expect) {
		t.Errorf("Expect %v, Got %v", expect, result)
	}
}
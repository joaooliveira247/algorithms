package main

import "fmt"

func main() {
	book := make(map[string]float64)
	book["Avocado"] = 1.79
	book["Milk"] = 1.79
	book["Apple"] = 0.67
	fmt.Println(book)
}
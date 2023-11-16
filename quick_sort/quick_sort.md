# 🛄💨 Quick sort

- In the best case *Quick sort* has O(n log n), to obtain the best case is recommended chose an aleatory *pivot*.

- In the worst case *Quick sort* has O(n²), it's defined by the choice of *pivot*.

- Recursive

- Divide and Conquer algorithm

*`How quick sort works:`*

```text
1. Find a “pivot” item in the array. This item is the basis for comparison for a single round. (the "pivot" can be the first item in an array)

2. Start a pointer (the left pointer) at the first item in the array.

3. Start a pointer (the right pointer) at the last item in the array.

4. While the value at the left pointer in the array is less than the pivot value, move the left pointer to the right (add 1). Continue until the value at the left pointer is greater than or equal to the pivot value.

5. While the value at the right pointer in the array is greater than the pivot value, move the right pointer to the left (subtract 1). Continue until the value at the right pointer is less than or equal to the pivot value.

6. If the left pointer is less than or equal to the right pointer, then swap the values at these locations in the array.

7. Move the left pointer to the right by one and the right pointer to the left by one.

8. If the left pointer and right pointer don’t meet, go to step 1.
```


## DC (Divide & conquer)

"D&C isn't a simple algorithm that you can apply a problem. Instead, it's 
**a way to think**"

`D&C code example`

[D&C](./dc.py)


## References

https://medium.com/karuna-sehgal/a-quick-explanation-of-quick-sort-7d8e2563629b

https://en.wikipedia.org/wiki/Quicksort
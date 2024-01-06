# 🔑📦 Hash table

- This is a composite data structure, 'cause generally you use arrays or linked lists to construct it.

- Key value data structure

### Big O notation of Hash Tables

| Operation | Average | Worst case |
| :-------: | :-----: | :--------: |
|  Search   |  O(1)   |    O(n)    |
|  Insert   |  O(1)   |    O(n)    |
|  Delete   |  O(1)   |    O(n)    |

## Hash Functions

Map a value with hash(integer) that will be an index of array.

![hash_function_diagram](https://khalilstemmler.com/img/blog/data-structures/hash-tables/hash-table.png)

```python
a = hash("banana")
b = hash("orange")
c = hash("banana")
print(f"a = {a}|b = {b}|c = {c}")
```

`>>> a = -6387414445991098205|b = 6535034116520114251|c = -6387414445991098205
`

- It needs to be consistent

  `Every same entry returns same hash.`

- It should map different words to different numbers.

  ` Every entry return a different hash`

<!-- ```python

has_function("banana")

[("banana", 12), ("orange", 6), ("egg", 3)]
``` -->

### Hash reductions

If your function generate a big hash, you can reduce using this formula:

$$hash \over len(array)$$

### Collisions

If you don't have a good hash function,
when you make a **hash reduction** it can generate the same "hash reduced"

`ex:`

```python
arr = [None, None, None]
banana -> 2 # After reduce
apple -> 1  # After reduce
orange -> 2 # After reduce
arr -> [None, ("apple", 2),("orange", 5)]
```

orange overwrite banana, you can think: "how i can fix it."

**1º - Increase the size of array.**

- with an big array the hash reduce can be preserved.

- spend a lot of memory.

**2º - Separate Chaining**

- Each bucket in the hashmap is implemented as a linked list or another data structure

- When a collision occurs, the key-value pairs with the same hash code are stored in the same bucket as a linked list

- This way, multiple key-value pairs can coexist at the same index without overwriting each other

**3º - Open Addressing**

- In this approach, when a collision occurs, the algorithm searches for the next available slot in the array

- Linear probing, quadratic probing, and double hashing are common techniques used to find the next available slot

- Linear probing, for example, involves searching for the next available slot by incrementing the index linearly until an empty slot is found

### Load factor

Hash tables use an array for storage, so you count the number of occupied slots in an array.

Load factor mensures how many empty slots remain in your hash table.

$$ Number\ of\ itens\ in\ HashTable\over Total\ number\ of\ slots $$

- If your HashTable has load factor by 3/4, you can resize twice her current size.

- You'll need re-insert all of itens in old HashTable.

---

`Code examples:`

Every language that you choose take an implementation of HashTable's, so you don't need implements it.

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px" />
Python](./python/main.py)

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width="20px"/>
Rust](./rust/src/lib.rs)

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="20px"/>
Go](./go/main.go)

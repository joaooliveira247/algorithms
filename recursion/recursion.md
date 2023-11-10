# 🔄 Recursion

Loops and recursions are same performance.

## Base case & recursive case

- ⬇️ Base case

    When the recursion finish

- 🔄 Recursion

    When the function invoke himself

```python
def regressive(i: int) -> None:
    print(i)
    if i <= 1: # Base case (end function)
        return
    else:
        regressive(i-1) # Recursive case (continue functions)
```

- 📥 Call stack

    The call stack works like a linked list, when u call the function "them"(compilers/interpreters) add an item in the top of stack; when him finish, him pop of stack

    ![call_stack_image](https://iq.opengenus.org/content/images/2019/04/r4.JPG)

    ```python
    def greet_2(name: str) -> None:
        print(f"How are you, {name} ?")

    def bye() -> None:
        print("Ok, bye.")
    ```

    ```python
    def greet(name: str) -> None:
        print(f"Hello, {name} !")
        greet_2(name)
        print("getting ready to say bye ")
        bye()
    ```

    <a href="https://imgur.com/tVWkGJv"><img src="https://i.imgur.com/tVWkGJv.png" title="source: imgur.com" /></a>

---

`Code examples:`

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="20px" />
Python](./python/main.py)

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg" width="20px"/>
Rust](./rust/src/lib.rs)

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg" width="20px"/>
Go](./go/main.go)
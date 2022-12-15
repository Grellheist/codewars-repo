# String repeat

---

**Definition**

Write a function that accepts an integer `n` and a string `a` as parameters, and returns a string of `s`repeated exactly `n` times.

**Examples (input -> output)**

```python
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
```

---

### Solution:

```python
def repeat_str(repeat, string):
    return string*repeat
```

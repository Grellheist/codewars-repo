# Reverse words

---

**Definition**

Complete the function that accepts a string parameter, and reverses each word
in the string. All spaces in the string should be retained.

**Examples**

```python
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
```

---

### Solution:

```python
def reverse_words(text):
    return ' '.join([character[::-1] for character in text.split(' ')])
```

# Snail

---

## Snail Sort

**Definition**

Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

```python
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```
For better understanding, please follow the numbers of the next array consecutively:

```python
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```
This image will illustrate things more clearly:

![snail](https://user-images.githubusercontent.com/20653258/206886323-887b7c00-0d86-42e8-919e-c8ebd4d6951d.png)

NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

---

### Solution:

```python
def snail(snail_map):
    s_list = []
    while(snail_map):
        s_list.append(snail_map.pop(0))
        snail_map = list(map(list, zip(*snail_map)))[::-1]
    return [inner for outer in s_list for inner in outer]


# Best practices would be to use numpy:
#import numpy as np
#
#def snail(array):
#    m = []
#    array = np.array(array)
#    while len(array) > 0:
#        m += array[0].tolist()
#        array = np.rot90(array[1:])
#    return m
```

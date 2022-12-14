# Range Extraction

---

**Definition**

A format for expressing an ordered list of integers is to use a comma separated
list of either individual integers or a range of integers denoted by the
starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is
not considered a range unless it spans at least 3 numbers. For example
"12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order
and returns a correctly formatted string in the range format.

**Example:**

```python
solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
```
Courtesy of rosettacode.org

---

### Solution:

```python
def solution(list):
    result = []
    buffer = []
    for number in sorted(list) + [None]:
        if not buffer:
            buffer.append(number)  # If the buffer list is empty, adds the element to it
        else:
			if number == buffer[-1]+1:  # If the buffer list is not empty, and
										# if the next number to the number is a successor, adds to the list
                buffer.append(number)
            else:
                if len(buffer) > 2:  # If the size of the buffer is more than 3, does the reduction
                    result.append(f'{buffer[0]}-{buffer[-1]}')
                else:
                    result.extend(str(x) for x in buffer)  # Otherwise, just adds the number normally
                buffer = [number]
    return ','.join(result)
```


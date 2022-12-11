# Human readable duration format

---

*Definition*

Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns `"now"`. Otherwise, the duration is expressed as a combination of `years`, `days`, `hours`, `minutes` and `seconds`.

It is much easier to understand with an example:

`
* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
`
*For the purpose of this Kata, a year is 365 days and a day is 24 hours.*

Note that spaces are important.

*Detailed rules*
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

---

### Solution:

```python
def format_duration(seconds):
    result = [] #Final result
    no_comma = [] #Removes the comma from the second to last element to add "and" after it
    auxiliary = [] #Helps remove the last comma
    pos = 0
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    day, hour = divmod(hour, 24)
    year, day = divmod(day, 365)
    if year > 1:
        result.append(str(year) + " years,")
    elif year == 1:
        result.append(str(year)+ " year,")
    if day > 1:
        result.append(str(day) + " days,")
    elif day == 1:
        result.append(str(day)+ " day,")
    if hour > 1:
        result.append(str(hour) + " hours,")
    elif hour == 1:
        result.append(str(hour)+ " hour,")
    if min > 1:
        result.append(str(min) + " minutes,")
    elif min == 1:
        result.append(str(min)+ " minute,")
    if sec > 1:
        result.append(str(sec) + " seconds,")
    elif sec == 1:
        result.append(str(sec)+ " second,")
    elif seconds == 0:
        return "now"
    if len(result) > 1: #Gets the position of the second to last element and removes the comma
        pos = result.index(result[-2])
        for letter in result[pos]:
            no_comma += letter
        no_comma.pop()
        result[pos] = ''.join(no_comma)
        result.insert(-1, "and")
    for letter in result[-1]: #Removes the final comma
        auxiliary += letter
    auxiliary.pop()
    result[-1] = ''.join(auxiliary)
    return ' '.join(result)
```

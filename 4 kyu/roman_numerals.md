# Roman Numerals Helper

---

**Definition**

Create a RomanNumerals class that can convert a roman numeral to and from an
integer value. It should follow the API demonstrated in the examples below.
Multiple roman numeral values will be tested for each helper method.

Modern Roman numerals are written by expressing each digit separately starting
with the left most digit and skipping any digit with a value of zero. In Roman
numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is
written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in
descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

**Examples**

```python
RomanNumerals.to_roman(1000) # should return 'M'
RomanNumerals.from_roman('M') # should return 1000
```

---

### Solution:

```python
class RomanNumerals:
    
    def to_roman(number):
        result = []
        if number >= 1000:
            while number >= 1000:
                number = number - 1000
                result.append('M')
        if number >= 900:
            while number >= 900:
                number = number - 900
                result += 'CM'
        if number >= 500:
            while number >= 500:
                number = number - 500
                result += 'D'
        if number >= 400:
            while number >= 400:
                number = number - 400
                result += 'CD'
        if number >= 100:
            while number >= 100:
                number = number - 100
                result += 'C'
        if number >= 90:
            while number >= 90:
                number = number - 90
                result += 'XC'
        if number >= 50:
            while number >= 50:
                number = number - 50
                result += 'L'
        if number >= 40:
            while number >= 40:
                number = number - 40
                result += 'XL'
        if number >= 10:
            while number >= 10:
                number = number - 10
                result += 'X'
        if number >= 9:
            while number >= 9:
                number = number - 9
                result += 'IX'
        if number >= 5:
            while number >= 5:
                number = number - 5
                result += 'V'
        if number >= 4:
            while number >= 4:
                number = number - 4
                result += 'IV'
        if number >= 1:
            while number >= 1:
                number = number - 1
                result += 'I'
        return ''.join(result)
    
    
    def from_roman(roman_num):
        roman_num = roman_num[::-1]
        roman_list = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        total = 0
        i = 0
        while i < len(roman_num):
            if i != len(roman_num) - 1:
                if roman_list[roman_num[i]] > roman_list[roman_num[i + 1]]:
                    total += roman_list[roman_num[i]] - roman_list[roman_num[i + 1]]
                    i += 1
                else:
                    total += roman_list[roman_num[i]]
            else:
                total += roman_list[roman_num[i]]
            i += 1
        return total
        return result

#Best solution I've found:
#import string
#from collections import OrderedDict
#
#class RomanNumerals:
#  @classmethod
#  def to_roman(self, num):
#    conversions = OrderedDict([('M',1000), ('CM',900), ('D', 500), ('CD',400), ('C',100), ('XC',90), ('L',50), ('XL',40),
#                               ('X',10), ('IX',9), ('V',5), ('IV',4), ('I',1)])
#    out = ''
#    for key, value in conversions.iteritems():
#      while num >= value:
#        out += key
#        num -= value
#    return out
#  
#  @classmethod
#  def from_roman(self, roman):
#    conversions = OrderedDict([('CM',900), ('CD',400), ('XC',90), ('XL',40), ('IX',9), ('IV',4), ('M',1000), ('D',500),
#                               ('C',100), ('L',50), ('X',10), ('V',5), ('I',1)])
#    out = 0
#    for key, value in conversions.iteritems():
#      out += value * roman.count(key)
#      roman = string.replace(roman, key, "")
#    return out
```

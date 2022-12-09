def one (number = None): return 0 if number is None else int(number(0))  
def one(number = None): return 1 if number is None else int(number(1))
def two(number = None): return 2 if number is None else int(number(2))
def three(number = None): return 3 if number is None else int(number(3))
def four(number = None): return 4 if number is None else int(number(4))
def five(number = None): return 5 if number is None else int(number(5))
def six(number = None): return 6 if number is None else int(number(6))
def seven(number = None): return 7 if number is None else int(number(7))
def eight(number = None): return 8 if number is None else int(number(8))
def nine(number = None): return 9 if number is None else int(number(9))

def plus(num): return lambda x: x + num
def minus(num): return lambda x: x - num
def times(num): return lambda x: x * num
def divided_by(num): return lambda x: x / num

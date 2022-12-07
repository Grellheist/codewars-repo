def pythagorean_triple(integers):
    square1 = integers[0] ** 2
    square2 = integers[1] ** 2
    square3 = integers[2] ** 2
    if square1 == square2 + square3:
        return True
    elif square2 == square1 + square3:
        return True
    elif square3 == square1 + square2:
        return True
    else:
        return False

# Way better solution:
#def pythagorean_triple(integers):
#    a, b, c = sorted(integers)
#    return a * a + b * b == c * c

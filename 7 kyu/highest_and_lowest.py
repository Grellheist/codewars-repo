def high_and_low(numbers):
    return sorted(numbers.split(' '), key=int)[-1] + ' ' + sorted(numbers.split(' '), key=int)[0]

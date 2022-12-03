def digital_root(n):
    return n if n < 10 else digital_root(sum([int(num) for num in str(n)]))
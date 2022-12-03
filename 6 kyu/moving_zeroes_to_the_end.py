def move_zeros(lst):
    return sorted(lst, key = lambda x: x == 0) #sorts by 0 and throws it at the end of the list
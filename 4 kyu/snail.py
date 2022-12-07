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

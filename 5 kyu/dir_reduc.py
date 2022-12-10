def dirReduc(arr):
    result = []
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'WEST': 'EAST', 'EAST': 'WEST'}
    
    for direction in arr:
        if len(result) == 0 or result[-1] != opposite[direction]:
            result.append(direction)
            continue
        result.pop()
    return result
def sum_array(arr):
    if not arr:
        return 0
    else:
        arr.sort()
        arr[0] = min
        arr[-1] = max
        result = 0
        for i in range (0, len(arr)):
            if not ((arr[i] == max) or (arr[i] == min)):
                result += arr[i]
        return result
        print(result)

import math

def solution(number):
    if number < 0:
        return 0
    else:
        sum_list = []
        number_list = []
        for digits in range(number-1, 0, -1):
            number_list.append(digits)
        for multiples in number_list:
            if (multiples % 3 == 0) or (multiples % 5 == 0):
                sum_list.append(multiples)
        result = math.fsum(sum_list) 
        return result

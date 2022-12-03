def find_it(numbers):
    answer = 0
    for digits in numbers:
        answer^=digits  #XOR will make sure the answer is only correct number since there's only one that appears an odd amount of times
    return answer
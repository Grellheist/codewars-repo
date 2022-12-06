def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    aux = []
    for letter in string:
        if letter in vowels:
            pass
        else:
            aux += letter
    return ''.join(aux)

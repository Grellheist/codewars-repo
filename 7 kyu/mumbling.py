def accum(string):
    return '-'.join(character.upper() + character.lower() * index for index, character in enumerate(string))

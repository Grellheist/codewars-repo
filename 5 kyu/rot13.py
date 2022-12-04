def rot13(message):
    list = []
    for character in message:
        list.append(conversion(character))
    return ''.join(list)


def conversion(character):
    if 65 <= ord(character) <= 90:
        new_letter = ord(character) + 13 # Converts the character to its integer equivalent + 13
        return chr(new_letter) if new_letter <= 90 else chr(64 + new_letter % 90) # Converts it back to a character and iterate again if it runs the entire list
    
    if 97 <= ord(character) <= 122:
        new_letter = ord(character) + 13
        return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)
    return character
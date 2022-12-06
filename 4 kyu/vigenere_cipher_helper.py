# source: https://github.com/mateuszmacheta/codewars-python/blob/master/Vigenere-Cipher-Helper.py

from itertools import cycle


class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        return self.inner(text)

    def decode(self, text):
        return self.inner(text, encode=False)

    def inner(self, text, encode=True):
        key = cycle(self.key)
        result = []
        for character in text:
            shift = self.alphabet.index(next(key)) # Shifts the key to match the text size
            if not encode:
                shift *= -1 # If the method is not calling 'encode' (but rather decode), shifts the opposite way
            if character not in self.alphabet:
                result.append(character) # Any character not in the alphabet returns as is
            else:
                character2 = self.alphabet[(self.alphabet.index(character) + shift) % len(self.alphabet)] # Does all the conversions 
                result.append(character2)
        return ''.join(result)
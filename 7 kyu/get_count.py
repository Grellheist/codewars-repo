def get_count(sentence):
    return len([letter for letter in sentence if letter in "aeiouAEIOU"])

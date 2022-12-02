from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    word = list(word)
    count_duplicate_letters = Counter(word)
    final_string = ""
    
    for letter in word:
        if count_duplicate_letters[letter] == 1:
            final_string += "("
        else:
            final_string += ")"
       
    return final_string

# Best solution:
# def duplicate_encode(word):
#     return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

def pig_it(sentence):
    word_list = sentence.split()
    pigified = ""
    for word in word_list:
        if word.isalpha():
            word = word[1:] + word[0] + "ay"
            pigified += word
            pigified += " "
        else:
            pigified += word
            pigified += " "
    pigified = pigified[:-1]
    return pigified
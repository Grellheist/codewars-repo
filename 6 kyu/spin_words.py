def spin_words(sentence):
    finalString = ""
    wordList = sentence.split()
    for word in wordList:
        if len(word) >= 5:
            word = word[::-1]
        finalString += word
        finalString += " "
    finalString = finalString[:-1]
    return finalString

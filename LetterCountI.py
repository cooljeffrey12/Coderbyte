#Using the Python language, have the function LetterCountI(str) take the str parameter
# being passed and return the first word with the greatest number of repeated letters.
# For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's
# (and 2 t's) and it comes before ever which also has 2 e's. If there are no words with repeating
#  letters return -1. Words will be separated by spaces.

def LetterCountI(str):
    strList = str.split(" ")
    print(strList)
    globalMax = 0
    wordMax = 0
    listLetter = []
    letterCount = []
    listWords = []
    result = ""

    for word in strList:
        for character in word:
            if character not in listLetter:
                listLetter.append(character)
                letterCount.append(1)
            else:
                letterCount[listLetter.index(character)]+=1
        for x in range(len(letterCount)):
            if letterCount[x] > wordMax:
                wordMax = letterCount[x]
        if wordMax > globalMax:
            globalMax = wordMax
            result = word
        listLetter.clear()
        letterCount.clear()
        print(wordMax)
        wordMax = 0

    return result

print(LetterCountI(input("Type in a String")))















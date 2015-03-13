def SecondGreatLow(arr):
    arr = arr.replace('[','').replace(']','')
    inputList = arr.split(" ")
    listInt = []
    for index in range(len(inputList)):
        listInt.append(int(inputList[index]))

    print(listInt)

    finalList = []
    seen = set()
    for entry in listInt:
        if entry not in seen:
            finalList.append(entry)
            seen.add(entry)

    finalList = sorted(finalList)
    print(finalList)
    secondGreatest = finalList[len(finalList)-2]
    secondLowest = finalList[1]

    result = str(secondLowest) + " " + str(secondGreatest)

    return result

print(SecondGreatLow(input("Type in an Array")))
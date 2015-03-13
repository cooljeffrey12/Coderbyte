def SecondGreatLow(arr):
    arr = arr.replace('[','').replace(']','')
    inputList = arr.split(" ")
    listInt = []
    for index in range(len(inputList)):
        listInt.append(int(inputList[index]))

    listInt = sorted(listInt)

    for entry in listInt:
        


    secondGreatest = listInt[len(listInt)-2]
    secondLowest = listInt[1]




print(SecondGreatLow(input("Type in an Array")))
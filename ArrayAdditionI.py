inputString = input("type in an array \n")
inputCapped = inputString.replace("[","").replace("]","")
arrString = inputCapped.split(" ")
input = list(map(int, arrString))

def ArrayAdditionI(input):
    input = sorted(input)
    largest = input.pop()
    return recursion(largest,input)

def recursion(target, array):
    if len(array) == 0:
        return target == 0
    else:
        n = array[0]
        array = array[1:]
        res = recursion(target,array) or recursion(target-n, array)
        return res

print(ArrayAdditionI(input))












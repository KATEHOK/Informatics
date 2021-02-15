def getTwinListWithMinRangeAndCurrentIdsNumIsPrimeAndAnotherIsNot(idsList, numsList):
    resRange = 99999999
    length = len(idsList)
    globalId = 0
    localId = idsList[0]
    for index in range(0, length):
        localRange = getRange(numsList[index])
        if localRange < resRange and isEven(numsList[index][idsList[index]]) and (not isEven(numsList[index][1 - idsList[index]])):
            resRange = localRange
            globalId = index
            localId = idsList[index]
    return [numsList[globalId], globalId, localId]


def getRange(numsList):  # Принимает на вход пару чисел и возвращает их разность
    resRange = numsList[0] - numsList[1]
    if resRange > 0:
        return resRange
    return -resRange


def isEven(num):  # Принимает на вход число, возвращает True, если оно чётное, иначе возвращает False
    return num % 2 == 0


myList = [
    [123, 125],
    [123, 126],
    [123, 128],
    [124, 123],
    [122, 123]
]

idList = [1, 1, 1, 1, 0]

print(getTwinListWithMinRangeAndCurrentIdsNumIsPrimeAndAnotherIsNot(idList, myList))

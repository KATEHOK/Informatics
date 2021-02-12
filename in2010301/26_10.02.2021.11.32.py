# C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/26/26.txt
def addLineToCurrentModel(line):
    arr = line.split(' ')
    price = int(arr[0])
    quantity = int(arr[1])
    model = arr[2]
    dadaDict[model].append([price, quantity])


def getIdListWithLowestPrice(inputList):
    localId = 0
    for idx in range(0, len(inputList)):
        if inputList[idx][0] < inputList[localId][0]:
            localId = idx
    return localId


def getSortedListByPriceLowHigh(inputList):
    outputList = []
    while len(inputList) > 0:
        newListsId = getIdListWithLowestPrice(inputList)
        outputList.append(inputList[newListsId])
        inputList.pop(newListsId)
    return outputList


dadaDict = {
    'A': [],
    'B': []
}
with open('C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/26/26.txt', 'r') as data:
    budget = int(data.readline().split(' ')[-1])
    for line in data:
        localArr = addLineToCurrentModel(line)
# print(dadaDict)
dadaDict = {
    'A': getSortedListByPriceLowHigh(dadaDict['A']),
    'B': getSortedListByPriceLowHigh(dadaDict['B'])
}
# print(dadaDict['A'])
# print('HEY')
# print(dadaDict['B'])
globalId = 0
quantity = 0
while budget > 0 and globalId < len(dadaDict['A']):
    while budget > 0 and dadaDict['A'][globalId][-1] > 0:
        if budget - dadaDict['A'][globalId][0] >= 0:
            quantity += 1
            lastNum = dadaDict['A'][globalId][0]
        budget -= lastNum
    globalId += 1
else:
    if budget < 0:
        budget += lastNum
print(budget, quantity)
# 4 76923

link = 'C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/27/'
# link = 'E:/Py_scr/stat_grad/Informatics/in2010301/27/'
fileName = input('Введите A или B: ')


# Принимает на вход список из строк, приводимых к целым числам, и возвращает список эквивалентных чисел
def getNumsListFromStrsList(strsList):
    result = []
    for el in strsList:
        result.append(int(el))
    return result


# Принимает на вход список из двух целых чисел и возвращает индекс большего из них
def getMaxNumsIdOfDoubleNumsList(inputList):
    if inputList[0] >= inputList[1]:
        return 0
    else:
        return 1


def isEven(num):  # Принимает на вход число, возвращает True, если оно чётное, иначе возвращает False
    return num % 2 == 0


# Принимает на вход список индексов и список пар чисел и возвращает сумму чисел по индексам из списка индексов
def getNumsSumByIds(idsList, numsList):
    resSum = 0
    length = len(idsList)
    for index in range(0, length):
        resSum += numsList[index][idsList[index]]
    return resSum


# Принимает на вход список индексов и список пар чисел, возвращает список из глобального и локального индексов наименьшего числа из списка
# def getIdsOfMinNumOfListById(idsList, numsList):
#     localId = idsList[0]
#     globalId = 0
#     length = len(idsList)
#     for index in range(0, length):
#         if numsList[index][idsList[index]] < numsList[globalId][localId]:
#             globalId = index
#             localId = idsList[index]
#     return [globalId, localId]


# Принимает на вход список индексов и список пар чисел, возвращает пару чисел с наименьшей разностью
def getTwinListWithMinRangeOneOfThemIsEvenAnotherIsNot(idsList, numsList):
    minRange = 9999999
    globalId = 0
    localId = idsList[0]
    length = len(idsList)
    for index in range(0, length):
        localRange = getRange(numsList[index])
        if localRange < minRange and (isEven(numsList[index][0]) != isEven(numsList[index][1])):
            minRange = localRange
            globalId = index
            localId = idsList[index]
    return [numsList[globalId], globalId, localId]


def getRange(numsList):  # Принимает на вход пару чисел и возвращает их разность
    resRange = numsList[0] - numsList[1]
    if resRange > 0:
        return resRange
    return -resRange


# Принимает на вход список индексов и список пар чисел, ищет среди пар чисел пару с наименьшей разностью, причем число с индексом из списка должно быть чётным, а другое - нечётным
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


def getTwinListWithMinRangeAndCurrentIdsNumIsNotPrimeAndAnotherIsPrime(idsList, numsList):
    resRange = 99999999
    length = len(idsList)
    globalId = 0
    localId = idsList[0]
    for index in range(0, length):
        localRange = getRange(numsList[index])
        if localRange < resRange and (not isEven(numsList[index][idsList[index]])) and isEven(numsList[index][1 - idsList[index]]):
            resRange = localRange
            globalId = index
            localId = idsList[index]
    return [numsList[globalId], globalId, localId]


with open(f'{link}27-{fileName}.txt', 'r') as data:
    firstLine = data.readline()
    localList = []
    for line in data:
        if fileName == 'A':
            # print(line.split('  '))
            localList.append(getNumsListFromStrsList(line.split('  ')))
        elif fileName == 'B':
            # print(line.split(' '))
            localList.append(getNumsListFromStrsList(line.split(' ')))
# print(localList)

# [[5544, 6521], [1449, 3580], [2984, 5984], [6164, 2583], [9588, 3467], [1440, 8636], [7706, 8023], [6847, 6023], [570, 1545], [7361, 5893], [4221, 5994], [3118, 5054], [1547, 4062], [780, 3433], [6926, 2390], [3702, 6714], [2278, 7180], [9156, 3466], [2294, 8733]] - A-file

choosenIdsList = []  # Список, хранящий индексы наибольщих чисел из каждой пары
evenCounter = 0  # Счётчик индексов чётных чисел

for array in localList:
    maxNumsId = getMaxNumsIdOfDoubleNumsList(array)
    if isEven(array[maxNumsId]):
        evenCounter += 1
    choosenIdsList.append(maxNumsId)

numsSum = getNumsSumByIds(choosenIdsList, localList)

# print(evenCounter, len(localList) - evenCounter, numsSum)
# 12 7 121501              A-file
# 2777 2778 36898732       B-file

# A
# print(getTwinListWithMinRangeOneOfThemIsEvenAnotherIsNot(choosenIdsList, localList))
# [[7706, 8023], 6, 1] - заменив нечетное число на четное мы минимально потеряем в общей сумме. Заменим...
# choosenIdsList[6] = 0
# print(getNumsSumByIds(choosenIdsList, localList))
# 121184

# B (1)
# print(getTwinListWithMinRangeAndCurrentIdsNumIsPrimeAndAnotherIsNot(
#     choosenIdsList, localList))
# [[3196, 3095], 3699, 0] заменим...
# choosenIdsList[3699] = 1
# print(getNumsSumByIds(choosenIdsList, localList))
# 36898631 - по итогу: нечетных чисел больше и сумма - нечетная, разность равна:
# print(3196 - 3095)
# 101

# B (2)
# 1 шаг:
# print(getTwinListWithMinRangeAndCurrentIdsNumIsNotPrimeAndAnotherIsPrime(
#     choosenIdsList, localList))
# [[6104, 6131], 5138, 1] - найдем разность:
# print(6131 - 6104)
# 27
# Заменим нечётное число на чётное => сумма-нечётная, чисел больше чётных
# choosenIdsList[5138] = 0
# 2 шаг:
# print(getTwinListWithMinRangeAndCurrentIdsNumIsNotPrimeAndAnotherIsPrime(
#     choosenIdsList, localList))
#     [[5451, 5404], 5171, 0]
# print(5451 - 5404) # разность - 47
# Заменим нечётное число на чётное => Сумма - чётная, больше чётных чисел, суммарная разность - 74, меньше, чем 101
# choosenIdsList[5171] = 1
# Найдём сумму:
# print(getNumsSumByIds(choosenIdsList, localList))
# 36898658
# print(36898658 > 36898631)
# True
# 121184*36898658

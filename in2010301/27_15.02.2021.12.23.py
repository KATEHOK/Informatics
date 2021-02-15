# link = 'C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/27/'
link = 'E:/Py_scr/stat_grad/Informatics/in2010301/27/'
fileName = input('Введите A или B: ')


def getNumsListFromStrsList(strsList):
    result = []
    for el in strsList:
        result.append(int(el))
    return result


with open(f'{link}27-{fileName}.txt', 'r') as data:
    print(data.readline())
    for line in data:
        if fileName == 'A':
            # print(line.split('  '))
            localList = getNumsListFromStrsList(line.split('  '))
            # print(localList)
        elif fileName == 'B':
            # print(line.split(' '))
            localList = getNumsListFromStrsList(line.split(' '))
            # print(localList)

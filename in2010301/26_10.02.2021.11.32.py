# C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/26/26.txt
def addLineToCurrentModel(line):
    arr = line.split(' ')
    price = int(arr[0])
    quantity = int(arr[1])
    model = arr[2]
    dadaDict[model].append([price, quantity])


dadaDict = {
    'A': [],
    'B': []
}
with open('C:/Users/Учитель/Desktop/Новая папка/Informatics/in2010301/26/26.txt', 'r') as data:
    budget = int(data.readline().split(' ')[-1])
    for line in data:
        localArr = addLineToCurrentModel(line)
print(dadaDict)

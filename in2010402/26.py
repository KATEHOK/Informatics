def isOdd(num):
    return num % 2 == 1


def isRight(num):
    return num in array


url = 'C:/Users/Учитель/Desktop/Dont_touch_me/Informatics/in2010402/files/26/26.txt'
array = []
oddArray = []
with open(url, 'r') as data:
    top = data.readline()
    for line in data:
        array.append(int(line))
        if isOdd(int(line)):
            oddArray.append(int(line))
# print(array)
# print(len(oddArray))
# print(isRight(708312995))
maxNum = 0
counter = 0
maxIndex = len(oddArray)
for index in range(maxIndex - 1):
    for n in range(index + 1, maxIndex):
        num = (oddArray[n] + oddArray[index]) // 2
        if isRight(num):
            counter += 1
            if num > maxNum:
                maxNum = num
print(counter, maxNum)

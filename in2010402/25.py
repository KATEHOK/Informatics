def isRight(num):
    counter = 0
    for x in range(1, num // 2 + 1, 2):
        if num % x == 0:
            counter += 1
            if counter > 5:
                return False
    if counter == 5:
        return True
    return False


for num in range(45000000, 50000001):
    if isRight(num):
        print(num)

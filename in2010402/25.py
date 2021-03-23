def isRight(num):
    counter = 0
    for x in range(3, num // 3 + 1, 2):
        if num % x == 0:
            counter += 1
            print(num, x, counter)
            if (num % 2 != 0 and counter > 3) or counter > 4:
                return False

    if (num % 2 != 0 and counter == 3) or counter == 4:
        return True
    return False


for num in range(45000000, 50000001):
    if isRight(num):
        print(num, 'RIGHT')
# -------^-WRONG-^--------

def isCorrectNum(num):
    counter = 0
    for divider in range(1, num // 2 + 1):
        if num % divider == 0:
            counter += 1
            if counter == 17:
                return True
    return False


counter = 0
for num in range(10001, 50001):
    if isCorrectNum(num):
        counter += 1
        if counter == 1:
            print(num)
print(counter)
# 10008
# 6585

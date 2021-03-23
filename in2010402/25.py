# def isRight(num):
#     counter = 0
#     for x in range(3, num // 3 + 1, 2):
#         if num % x == 0:
#             counter += 1
#             print(num, x, counter)
#             if (num % 2 != 0 and counter > 3) or counter > 4:
#                 return False

#     if num % 2 != 0:
#         if counter == 3:
#             return True
#     elif counter == 4:
#         return True
#     return False


# for num in range(45000000, 50000001):
#     if isRight(num):
#         print(num, 'RIGHT')
# -------^-WRONG-^--------
# print(50000000 // 3 + 1)
# obj = {}
# for num in range(1, 16666668, 2):
#     maxNum = 25000000
#     for x in range(num, maxNum):
#         result = x * num
#         if isInRange(result):
#             result = str(result)
#             if not (result in obj):
#                 obj[result] = [num]
#             else:
#                 obj[result].append(num)
#             if x % 2 != 0:
#                 obj[result].append(x)
# print(len(obj))
###############################################

# print(45000000 ** 0.25) # 81.903625881272
# print(50000000 ** 0.25) # 84.08964152537145

# print(1, 83, 83 ** 2, 83 ** 3, 83 ** 4)
# 1 83 6889 571787 47458321

# 5 простых чисел, помноженных на двойку в степени
def isInRange(num):
    return num >= 45000000 and num <= 50000000


def isPrime(num):
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            return False
    return True


def getDoubleNum(prime):
    copy = prime
    while prime < 45000000:
        prime *= 2
    return prime // copy


for num in range(1, 85):
    if isPrime(num):
        local = num ** 4
        support = getDoubleNum(local)
        answer = local * support
        if isInRange(answer):
            print(answer)
# 45265984
# 45212176
# 48469444
# 47458321

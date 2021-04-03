# def isPrime(num):
#     for x in range(2, num // 2 + 1):
#         if num % x == 0:
#             return False
#     return True

# print(90000 ** (1/3))  # 45
# print(50000 ** (1/3))  # 36
# counter = 0
# for num in range(36, 45):
#     if isPrime(num):
#         if num ** 3 > 50000 and num ** 3 <= 90000:
#             counter += 1
#             if counter == 1:
#                 print(num ** 3)
# print(counter)
################################################################


# def isRight(num):
#     array = [num]
#     length = 1
#     for n in range(1, num // 2 + 1):
#         if isPrime(n) and num % n == 0:
#             if not (n in array):
#                 array.append(n)
#                 length += 1
#                 if length > 3:
#                     return False
#     if length == 3:
#         return True
#     return False


# counter = 0
# for num in range(50001, 90001):
#     print(num)
#     if isRight(num):
#         counter += 1
#         if counter == 1:
#             print(num, 'FIRST')  # 50003
# print(counter, 'STOP')
########################################


# def isInRange(num):
#     return num >= 50001 and num <= 90000


# array = []
# for diver in range(2, 45001):
#     if not isPrime(diver): # (and isInRange(num))
#         continue
####################################################
# def isInRange(num):
#     return num >= 50001 and num <= 90000


def isPrime(num):
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            return False
    return True


# def getDoubleNum(prime):
#     copy = prime
#     while prime < 50001:
#         prime *= 2
#     return prime // copy


# for num in range(1, 100):
#     if isPrime(num):
#         local = num ** 3
#         support = getDoubleNum(local)
#         answer = local * support
#         if isInRange(answer):
#             print(answer)
# a = [50653, 54872, 55296, 59582, 64000, 65536, 68921, 70304, 78608, 79507, 85184, 87808]
###############################################################
primes = []
for num in range(2, 45001):
    if isPrime(num):
        primes.append(num)
# print(len(primes)) # считает десять секунд
quantity = 0
# for num in range(50001, 90001):
#     counter = 0
#     for n in primes:
#         if num % n == 0:
#             counter += 1
#             if counter > 3:
#                 break
#     if counter == 3:
#         quantity += 1
#         if quantity == 1:
#                         print(num) # 50001
#             print(quantity) # 15587
# print(primes)
# for num in primes:
#     if 50001 % num == 0:
#         print(num) # 3 7 2381

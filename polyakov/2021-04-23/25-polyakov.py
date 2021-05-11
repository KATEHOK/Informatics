# (Дермовариант 2021) Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [174457; 174505], числа, имеющие ровно два различных натуральных делителя, не считая единицы и самого числа. Для каждого найденного числа запишите эти два делителя в таблицу на экране с новой строки в порядке возрастания произведения этих двух делителей. Делители в строке таблицы также должны следовать в порядке возрастания.


def isPrime(num):
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            return False
    return True


def isInRange(num):
    return num >= 174457 and num <= 174505


def getDoubleDiver(num):
    counter = 0
    while num < 174457:
        num *= 2
        counter += 1
    return 2 ** counter


def getDivers(num):
    array = []
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            array.append(x)
    return list(set(array))


for num in range(174457, 174506):
    if isPrime(num):
        continue
    divers = getDivers(num)
    if len(divers) == 2:
        print(divers[0], '*', divers[1], '=',
              divers[0] * divers[1], '<--', num)
# 58153 3 <-- 174459
# 24923 7 <-- 174461
# 59 2957 <-- 174463
# 13 13421 <-- 174473
# 1171 149 <-- 174479
# 34897 5 <-- 174485
# 827 211 <-- 174497
# 2 87251 <-- 174502

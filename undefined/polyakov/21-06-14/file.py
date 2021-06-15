from typing import Counter


def sixth():
    copy = 10000
    n = 99999999
    while n >= 1000:
        s = copy - 1
        copy = s
        n = 0
        while 400 < s*s:
            s = s - 1
            n = n + 3
        print(copy, n)
    else:
        print('STOP:', copy)  # 353


# sixth()

# print(5 * 63 / (2 * 4.5)) # 35
# print((7 * 6 * 5 * 4 * 3) - (5 * 4 * 3 * 2 * 2) * 10) # 120

def twevwe(ones, threes):
    inpStr = '1' * ones + '3' * threes
    while '11' in inpStr:
        inpStr = inpStr.replace('11', '2', 1)
        if '22' in inpStr:
            inpStr = inpStr.replace('22', '3', 1)
        if '33' in inpStr:
            inpStr = inpStr.replace('33', '1', 1)
    else:
        print(inpStr)


# twevwe(2019, 2119) # 313
def fifteenth():
    copy = 0
    while True:
        check = True
        a = copy + 1
        copy = a
        for x in range(1, 10000):
            if (x % a == 0 and x % 21 == 0 and x % 18 != 0):
                check = False
        if check:
            print(copy)
            return


def f(n):
    if n > 25:
        return n * n + 4 * n + 3
    if n % 3 == 0:
        return f(n + 1) + 2 * f(n + 4)
    return f(n + 2) + 3 * f(n + 5)

# fifteenth() # 18


def sixteenth():
    # Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
    # F(n) = n*n + 4*n + 3, при n > 25
    # F(n) = F(n+1) + 2*F(n+4), при n ≤ 25, кратных 3
    # F(n) = F(n+2) + 3*F(n+5), при n ≤ 25, не кратных 3
    # Определите количество натуральных значений n из отрезка [1; 1000], для которых сумма цифр значения F(n) равна 24.
    counter = 0
    for n in range(1, 1001):
        res = f(n)
        res = str(res)
        mySum = 0
        for l in res:
            mySum += int(l)
        if mySum == 24:
            counter += 1
    print(counter)


# sixteenth() # 100
def isCorr17(n):
    return n % 7 == 0 and n % 11 != 0 and n % 13 != 0 and n % 17 != 0 and n % 23 != 0


def seventeenth():
    # Рассматривается множество целых чисел, принадлежащих отрезку [1512;13202], которые делятся на 7 и не делятся на 11, 13, 17 и 23. Найдите количество таких чисел и максимальное из них.
    # В ответе запишите два числа через пробел: сначала количество, затем максимальное число.
    counter = 0
    for n in range(13202, 1511, -1):
        if isCorr17(n):
            counter += 1
            if counter == 1:
                print('MAX:', n)  # 13188
    print(counter)


# seventeenth()  # 1265

def twentysecond():
    copy = 0
    counter = 0
    while True:
        x = copy + 1
        copy = x
        a = 0
        b = 0
        while x > 0:
            a = a + 1
            b = b + (x % 10)
            x = x // 10
        # print(a, b)
        if a == 2 and b == 12:
            counter += 1
            print('NICE', copy, counter)


# twentysecond()

def twentyfour():
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-06-14/24-s1.txt'
    counter = 0
    with open(link, 'r') as data:
        for line in data:
            if line.count('J') > line.count('E'):
                counter += 1
                # print('NICE')
    print(counter)


# twentyfour() # 482
def getDivers(n):
    result = [1, n]
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            result.append(x)
    result.sort()
    return result


def twentyfifth():
    # Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [338472; 338494], числа, имеющие ровно 4 различных делителя. В ответе для каждого найденного числа запишите два его наибольших делителя в порядке возрастания.
    for n in range(338472, 338495):
        tmp = getDivers(n)
        if len(tmp) == 4:
            print(tmp[2:])


# twentyfifth()

def twentysixth():
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-06-14/26-j2.txt'
    with open(link, 'r') as data:
        count = int(data.readline())
        # mySum = 0
        # # for line in data:
        # #     mySum += int(line)
        # # middle = mySum / count
        # # print(middle)
        # middle = 5003.8890831109165
        # myArr = []
        # for line in data:
        #     myArr.append(int(line))
        # myArr.sort()
        # print(len(myArr)) # 1000001
        # print(myArr[500000]) # 5007
        # print(myArr.count(5007)) # 81
        # i = 0
        # newArr = []
        # while i < len(myArr):
        #     if myArr[i] != 5007:
        #         newArr.append(myArr[i])
        #     i += 1
        # print(len(newArr))
        counter = 0
        for line in data:
            if int(line) > 5003 and int(line) <= 5007:
                counter += 1
        print(counter)  # 340


# twentysixth()
def second():
    # Логическая функция F задаётся выражением (x ∧ ¬y) ∨ (y ≡ z) ∨ w.
    data = [False, True]
    logs = []
    for x in data:
        for y in data:
            for z in data:
                for w in data:
                    if not ((x and (not y)) or (y == z) or w):
                        logs.append([x, y, z, w])
    for item in logs:
        print(item)


second()

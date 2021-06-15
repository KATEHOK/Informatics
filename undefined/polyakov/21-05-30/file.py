def sixth():
    n = 2000
    copy = -1
    while n <= 2000:
        s = copy + 1
        copy = s
        n = 0
        while s < s * s:
            s -= 1
            n += 3
        print(n)
    else:
        print('STOP', copy)  # 668
# sixth()


def twelve(o, t):
    inStr = '1' * int(o) + '2' * int(t)
    while '222' in inStr:
        inStr = inStr.replace('222', '1', 1)
        if '111' in inStr:
            inStr = inStr.replace('111', '2', 1)
    else:
        print(inStr)  # 1122


# twelve(2019, 2119)
def fifteenth():
    copy = 0
    while True:
        a = copy + 1
        copy = a
        # status = True
        counter = 0
        for x in range(1, 1000):
            if x % a == 0 and (x % 28 == 0 and x % 42 != 0):
                # status = False
                counter += 1
                # break
        # if status:
        if counter == 0:
            return copy


# print(fifteenth()) # 3

def f(n):
    if n > 30:
        return n * n + 5 * n + 4
    elif n % 2 == 0:
        return f(n + 1) + 3 * f(n + 4)
    return 2 * f(n + 2) + f(n + 5)


def sixteenth():
    counter = 0
    for n in range(1, 1001):
        value = str(f(n))
        tmp = 0
        for l in value:
            tmp += int(l)
        if tmp == 27:
            counter += 1
    return counter  # 137


# print(sixteenth())
def isTrueToST(n):
    return n % 7 != 0 and n % 13 != 0 and n % 17 != 0 and n % 19 != 0 and n % 11 == 0


def seventeenth():
    counter = 0
    for n in range(9680, 1605, -1):
        print(n)
        if isTrueToST(n):
            counter += 1
            if counter == 1:
                print('max', n)
    print('count', counter)


# 9680
# 519
# seventeenth()
# print(9680 % 7, 9680 % 13, 9680 % 17, 9680 % 19, 9680 % 11)
def twentySecond():
    a = 0
    b = 0
    copy = 9999
    while a != 4 or b != 2:
        x = copy + 1
        copy = x
        a = 0
        b = 0
        while x > 0:
            y = x % 10
            if y > 3:
                a += 1
            if y < 8:
                b += 1
            x = x // 10
        print(a, b)
    else:
        print('STOP', copy)  # 14888


# twentySecond()
def twentyfourth():
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-05-30/24-j5.txt'
    with open(link, 'r') as data:
        line = data.readline()
    print(line.count('SOCKCOS'))


# twentyfourth()
def isPrime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True


def getDivers(n):
    ans = [1, n]
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            ans.append(x)
    return ans


def twentyFifth():
    for n in range(164700, 164753):
        divers = getDivers(n)
        if len(divers) == 6:
            divers.sort()
            print(divers)
# [1, 2, 4, 41177, 82354, 164708]
# [1, 3, 9, 18301, 54903, 164709]
# [1, 2, 4, 41179, 82358, 164716]
# [1, 2, 4, 41183, 82366, 164732]


# twentyFifth()
def twentysixth():
    lib = [0]
    while len(lib) < 100:
        lib.append(0)
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-05-30/26-j1.txt'
    with open(link, 'r') as data:
        trash = data.readline()
        for line in data:
            lib[int(line)] += 1
    counter = 0
    for x in range(1, 50):
        print(f'{x}: {lib[x]}, {100 - x}: {lib[100 - x]}')
        counter += min(lib[x], lib[100 - x])
    print(f'50: {lib[50]}')
    counter += lib[50] // 2
    print('END:', counter)  # 3845


# twentysixth()
# python E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-05-30/file.py

from typing import Counter


def second():
    poss = [False, True]
    answer = []
    for x in poss:
        for y in poss:
            for z in poss:
                if not ((not ((not x) or (not z))) or (x == y)):
                    answer.append([x, y, z])
    for el in answer:
        print(el)
    # [False, True, False]
    # [False, True, True]
    # [True, False, False]
# second()


def sixth():
    s = 33
    n = 1
    while s > 0:
        s -= 7
        n *= 3
    print(n)


# sixth()

# print(88 * 4 * 3 // 264) # 4

# print(7*6*5*4*3*2 - (6*5*4*3*2 + 2*4*3*2*5))  # 4080

def twelwe():
    inpStr = 193 * '5'
    while '333' in inpStr or '555' in inpStr:
        if '555' in inpStr:
            inpStr = inpStr.replace('555', '3', 1)
        else:
            inpStr = inpStr.replace('333', '5', 1)
    print(inpStr)


# twelwe() # 55335
# print(2**6 + 2**5 + 2**4 + 2**3 + 2**1) # 122
# print(1+1064+143+1+1) # 1210
def fifteenth():
    maxN = 1000
    a = 101
    while True:
        a -= 1
        counter = 0
        for x in range(1, maxN + 1):
            for y in range(1, maxN + 1):
                if (y + 4 * x != 120) or (x > a) or (y > a):
                    counter += 1
        if counter == maxN ** 2:
            print('STOP:', a)
            return


# fifteenth() # 23
def sixteenth(n=3):
    if n < 6:
        return n + \
            sixteenth(n + 3) * sixteenth(2 * n)
    else:
        return n * 2


# print(sixteenth()) # 147
def seventeenth():
    # last = 27
    # array = [27]
    # for n in range(27, 900001):
    #     if n // last == 2:
    #         array.append(n)
    #         last = n
    # print(array)
    array = [27, 54, 108, 216, 432, 864, 1728, 3456, 6912,
             13824, 27648, 55296, 110592, 221184, 442368, 884736]
    x = 16
    counter = 0
    while x > 0:
        x -= 1
        tmp = str(array[x])
        ar = []
        checker = True
        for l in tmp:
            if l in ar:
                checker = False
            else:
                ar.append(l)
        if checker:
            counter += 1
            if counter == 1:
                print(tmp)
    print(counter)
# 27648
# 11

# seventeenth()


def twentysecond():
    m = 0
    copy = 100
    while m != 35:
        x = copy + 1
        copy = x
        l = x - 15
        m = x + 20
        while l != m:
            if l > m:
                l -= m
            else:
                m -= l
        print(x, m)
    else:
        print(x)  # 120


# twentysecond()
def twentyfour():
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-06-20/24-5.txt'
    with open(link, 'r') as data:
        inpStr = data.readline()
    curLen = 1
    maxLen = 1
    last = ''
    for l in inpStr:
        if l == ')' and last == l:
            curLen += 1
            if curLen > maxLen:
                maxLen = curLen
        else:
            curLen = 1
            last = l
    print(maxLen)  # 17


# twentyfour()
def isPrime(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True


def twentyfifth():
    # print(50034679 ** 0.25, 92136895 ** 0.25) # 84.10421845796056 97.97344813341063
    for n in range(85, 98):
        if isPrime(n):
            print(n ** 4, n ** 3)
# 62742241 704969
# 88529281 912673


# twentyfifth()
def twentyseventh():
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-06-20/27-12'
    even = []
    odd = []
    with open(f'{link}b.txt', 'r') as data:  # a || b
        header = data.readline()
        for line in data:
            n = int(line)
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
    # print(len(even), len(odd))
    counter = 0
    for e in range(len(even) - 1):
        for i in range(e + 1, len(even)):
            if (even[e] * even[i]) % 6 == 0:
                counter += 1
    for e in even:
        for o in odd:
            if (e * o) % 6 == 0:
                counter += 1
    print(counter)
# A: 47
# B: 745460178
# twentyseventh()

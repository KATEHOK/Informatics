def sixth():
    copy = 0
    s = 0
    while s == copy:
        s = copy + 1
        copy = s
        n = 100
        while s - n >= 100:
            s += 20
            n += 40
        print(s)
    else:
        print('STOP:', copy)  # 200


# sixth()

def twelwe():
    inpStr = 170 * '7'
    while '777' in inpStr:
        inpStr = inpStr.replace('77', '2', 1)
        if '22' in inpStr:
            inpStr = inpStr.replace('22', '7', 1)
        print(inpStr)
    print('STOP', inpStr)


# twelwe()
def fifteenth():
    a = 10000
    checker = True
    while checker:
        a -= 1
        checker = False
        for x in range(1, 1001):
            if not ((not (x % a != 0 and x % 21 == 0)) or x % 14 == 0):
                checker = True
    else:
        print(a)  # 21


# fifteenth()
def f(n):
    if n <= 3:
        return n
    if n % 2 == 0:
        return 2 * n + f(n - 1)
    return n * n + f(n - 2)


def sixteenth():
    counter = 0
    for n in range(1, 101):
        tmp = f(n)
        if tmp % 3 == 0:
            counter += 1
    print(counter)  # 32


# sixteenth()
def seventeenth():
    mySum = 0
    count = 0
    for n in range(3672, 9118):
        if n % 3 == 2 and n % 5 == 4:
            mySum += n
            count += 1
    print(count, mySum)


# seventeenth()
def twentysecond():
    copy = 100
    m = 0
    while m != 35:
        x = copy + 1
        copy = x
        l = x - 20
        m = x + 15
        while m != l:
            if l > m:
                l -= m
            else:
                m -= l
        print(copy, m)
    else:
        print('STOP', copy)  # 125


# twentysecond()
def twentyfourth():
    link = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-06-15/24-5.txt'
    with open(link, 'r') as data:
        counter = 0
        inpStr = data.readline()
        for i in range(len(inpStr)):
            if inpStr[i] == '(':
                counter += 1
                if counter == 10000:
                    print(i + 1)  # 20137
                    return


# twentyfourth()
def getDivers(n):
    arr = [1, n]
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            arr.append(x)
    arr.sort()
    return arr


def twentyfifth():
    maxL = 0
    maxD = 0
    for n in range(286564, 287271):
        arr = getDivers(n)
        if len(arr) == maxL:
            maxD = arr[-2]
        elif len(arr) > maxL:
            maxL = len(arr)
            maxD = arr[-2]
    print(maxL, maxD)  # 112 143520


# twentyfifth()
def twentyseventh():
    # произведение делится на 13, если хотя бы один множитель делится на 13
    # сумма нечетна, если одно из слагаемых четное, а другое нечетное
    firstLink = 'E:/Py_scr/stat_grad/Informatics/undefined/polyakov/21-06-15/27-16'
    with open(f'{firstLink}b.txt', 'r') as data:  # 'a' можно менять на 'b' для смены файла
        header = data.readline()
        catalog = []
        for line in data:
            catalog.append(int(line))
        counter = 0
        for i in range(len(catalog) - 1):
            for j in range(i + 1, len(catalog)):
                if (catalog[i] % 2 != catalog[j] % 2) and ((catalog[i] * catalog[j]) % 13 == 0):
                    counter += 1
    # print(len(catalog))
    print(counter)


# twentyseventh()
# A: 19
# B: 132286186

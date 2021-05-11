def editor(num):
    myStr = num * '5'
    while '5555' in myStr:
        myStr = myStr.replace('5555', '33', 1)
        if '333' in myStr:
            myStr = myStr.replace('333', '5', 1)
    return myStr


# print(editor(150)) # 5355

def f(num):
    if num <= 3:
        return num
    if num % 2 == 0:
        return f(num - 1) + 2 * f(num // 2)
    return f(num - 1) + f(num - 3)


def isTrue():
    num = 1
    counter = 0
    while True:
        temp = f(num)
        if temp < 100000000:
            counter += 1
            print(f'NUM: {num}, COUNTER: {counter}')
        else:
            print(num, counter)
        num += 1


# isTrue()

def sevenTeenth(minRange, maxRange):
    counter = 0
    mySum = 0
    for num in range(minRange, maxRange + 1):
        if num % 2 == 0 and num % 13 > 0:
            counter += 1
            mySum += num
    return f'count: {counter}, sum: {mySum}'


# print(sevenTeenth(2595, 8401)) # count: 2679, sum: 14728918

def twentySecond():
    copy = 100
    status = True
    while status:
        copy += 1
        x = copy
        l = x - 16
        m = x + 16
        while l != m:
            if l > m:
                l -= m
            else:
                m -= l
        if m == 16:
            return f'X = {copy}'


# print(twentySecond()) # X = 128

def isSimple(n):
    for x in range(2, n // 2 + 1):
        if n % x == 0:
            return False
    return True


def twentyFifth():
    counter = 0
    for num in range(4301614, 4301718):
        if isSimple(num):
            counter += 1
            print(f'number: {counter}, num: {num}')


# twentyFifth()
# number: 1, num: 4301623
# number: 2, num: 4301669
# number: 3, num: 4301699
# number: 4, num: 4301701
# number: 5, num: 4301707

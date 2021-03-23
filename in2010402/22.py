copy = 0
a = 0
b = 0
while a != 3 or b != 11:
    x = copy + 1
    copy = x
    k = x % 9
    a = 0
    b = 0
    while x > 0:
        d = x % 9
        if d == k:
            a += 1
        b += d
        x //= 9
    print(a, b, copy)
print('stop')

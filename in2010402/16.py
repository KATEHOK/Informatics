def f(num):
    if num == 0:
        return 0
    if num % 3 == 0:
        return f(num // 3)
    return (num % 3) + f(num - (num % 3))


num = 0
while f(num) != 9:
    num += 1
else:
    print(num)

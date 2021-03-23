def isPrime(num):
    for x in range(2, num // 2 + 1):
        if num % x == 0:
            return False
    return True


# print(90000 ** (1/3)) # 45
# print(50000 ** (1/3)) # 36
counter = 0
for num in range(36, 45):
    if isPrime(num) and num ** 3 > 50000 and num ** 3 <= 90000:
        counter += 1
        if counter == 1:
            print(num ** 3)
print(counter)

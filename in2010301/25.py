def isPrime(num):
    for x in range(2, num // 2 + 2):
        if num % x == 0:
            return False
    return True


result = []
minNum = int((101000000 // 2) ** 0.5) - 10
maxNum = int((102000000 // 2) ** 0.5) + 10
for num in range(minNum, maxNum):
    if isPrime(num):
        x = (num ** 2) * 2
        if x >= 101000000 and x <= 102000000:
            result.append(x)
print(result)
# [101075762, 101417282, 101588258, 101645282]

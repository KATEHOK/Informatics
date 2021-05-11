# Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями:
# F(n) = n + 15, при n ≤ 5
# F(n) = F(n//2) + n*n*n - 1, при чётных n > 5
# F(n) = F(n-1) + 2*n*n + 1, при нечётных n > 5
# Здесь // обозначает деление нацело. Определите количество натуральных значений n из отрезка [1; 1000], для которых значение F(n) содержит не менее двух цифр 8.

def workMan(num):
    if num <= 5:
        return num + 15
    elif num % 2 == 0:
        return workMan(num // 2) + num ** 3 - 1
    else:
        return workMan(num - 1) + 2 * (num ** 2) + 1


def isNumRight(num):
    num = str(workMan(num))
    return num.count('8') >= 2


counter = 0
for num in range(1, 1001):
    if isNumRight(num):
        counter += 1
print(counter)  # 164

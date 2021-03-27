array = [1, 2, 3, 4, 5, 6, 9, 10, 12, 13, 15, 18, 20, 26, 30, 36,
         39, 40, 45, 52, 60, 65, 78, 90, 130, 156, 180, 195, 260, 390, 780]
num = 0
counter = 0
while counter != len(array):
    num += 1
    counter = 0
    for n in array:
        if num % n == 0:
            counter += 1
else:
    print(num)

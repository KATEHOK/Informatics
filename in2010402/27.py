url = 'C:/Users/Учитель/Desktop/Dont_touch_me/Informatics/in2010402/files/27/27-'
array = []
with open(f'{url}A.txt', 'r') as data:
    count = data.readline()
    for line in data:
        # print(line)

        array.append(int(line))

##########################
# array.sort()
# [25, 56, 136, 193, 203, 206, 215, 217, 246, 268, 273, 286, 308, 323,
# 364, 375, 376, 406, 432, 487, 503, 513, 516, 523, 566, 617, 667,
# 691, 694, 724, 775, 832, 838, 850, 874, 880, 894, 898, 919, 951]
# print(25 + 56 + 246)  # 327
# print(array)

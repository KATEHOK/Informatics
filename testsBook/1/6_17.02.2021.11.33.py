# # checker = True
# s = 4096
# while s > 0:
#     sCopy = s
#     n = 1
#     # print(s, n)
#     while s * n < 4096:
#         s = s // 2
#         n *= 4
#     if n == 1024:
#         print(sCopy)
#     s = sCopy - 1
for s in range(100, 129):
    n = 1
    while s * n < 4096:
        s = s // 2
        n *= 4
    print(n)

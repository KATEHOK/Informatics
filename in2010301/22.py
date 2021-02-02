for x in range(0, 363):
    xCopy = x

    m = 0
    s = 0
    while x > 0:
        d = x % 8
        s += d
        if d > m:
            m = d
        x = x // 8
    print(xCopy, m, s)
    if m == 5 and s == 12:
        break
# 173 5 12

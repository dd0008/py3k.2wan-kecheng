# 开发人：d
# 开发时间：2021/12/29,8:38
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

m = 0
for t in fibon(1):
    print(t)
    m = m + 1
    if m == 10:
        break





























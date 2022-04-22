# 解説AC


a, b, x = map(int, input().split())

if x > a * 10 ** 9 + b * 10:
    print(0)
    exit()

# 商
k = x // a
# 桁数
l = len(str(k)) if k != 0 else 1

if a * k + b * l <= x:
    print(k)
else:
    print(k - 10 ** (l - 1))

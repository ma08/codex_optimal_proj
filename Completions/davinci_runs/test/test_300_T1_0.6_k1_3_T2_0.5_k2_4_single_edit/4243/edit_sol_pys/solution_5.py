

from collections import defaultdict

def happiness(x, n):
    d = defaultdict(int)  # d: 各種額の回数
    for i in n:
        d[i] = x // i
        x %= i
    return 1000 * d[500] + 5 * d[5]  # 幸せ度を計算

x = int(input())
print(happiness(x))

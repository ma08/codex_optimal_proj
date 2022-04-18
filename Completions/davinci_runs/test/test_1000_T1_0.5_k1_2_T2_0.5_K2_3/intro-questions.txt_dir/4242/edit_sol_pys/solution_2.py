import math

def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

a, b, k = map(int, input().split())  # 入力

g = gcd(a, b)  # 最大公約数

divisors = []  # 約数のリスト
for i in range(1, int(math.sqrt(g)) + 1):
    if g % i == 0:
        divisors.append(i)
        if i != g // i:
            divisors.append(g // i)

divisors.sort(reverse=True)  # 降順にソート

print(divisors[k - 1])

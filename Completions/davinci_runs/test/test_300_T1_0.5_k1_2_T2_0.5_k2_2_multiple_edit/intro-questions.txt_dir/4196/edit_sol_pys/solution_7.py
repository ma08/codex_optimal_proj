from fractions import gcd  # 最大公約数

n = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, gcd(a_list[i], a_list[j]))

print(ans)

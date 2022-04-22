def gcd(a, b):
    if a < b:
        a, b = b, a
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a


n = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, gcd(a_list[i], a_list[j]))

print(ans)

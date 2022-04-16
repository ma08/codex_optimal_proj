def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)



n = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, gcd(a_list[i], a_list[j]))

print(ans)

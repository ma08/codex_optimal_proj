

n = int(input())
a_list = list(map(int, input().split()))

ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = max(ans, a_list[i] * a_list[j] / gcd(a_list[i], a_list[j]))

print(ans)

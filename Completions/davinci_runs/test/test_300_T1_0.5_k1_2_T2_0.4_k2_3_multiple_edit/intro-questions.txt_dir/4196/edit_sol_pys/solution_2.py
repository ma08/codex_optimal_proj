def gcd(a, b): return a if b == 0 else gcd(b, a % b)


n = int(input())
a_list = list(map(int, input().split()))

ans = max(gcd(a_list[i], a_list[j]) for i in range(n) for j in range(i + 1, n))

print(ans)

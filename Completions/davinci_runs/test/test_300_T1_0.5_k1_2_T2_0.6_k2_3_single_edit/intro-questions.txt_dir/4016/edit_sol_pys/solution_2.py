
n, k = map(int, input().split())
t = input()

ans = t[0: k - 1] + t[k - 1]
n = n - k

print(ans)

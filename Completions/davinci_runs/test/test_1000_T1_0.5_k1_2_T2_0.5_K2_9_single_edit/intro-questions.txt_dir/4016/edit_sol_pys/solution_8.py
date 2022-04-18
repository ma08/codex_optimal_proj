
n, k = map(int, input().split())
t = input()

ans = t[(k - 1) % n] * n

print(ans)

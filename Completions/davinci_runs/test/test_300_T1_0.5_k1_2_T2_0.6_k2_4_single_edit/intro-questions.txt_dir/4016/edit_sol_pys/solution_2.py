# AtCoder Beginner Contest 157
# A - Duplex Printing

n, k = map(int, input().split())
t = input()

ans = ""
for i in range(n):
    if i < (k - 1) % n:
        ans += t[i]
    else:
        ans += t[(k - 1) % n]

print(ans)

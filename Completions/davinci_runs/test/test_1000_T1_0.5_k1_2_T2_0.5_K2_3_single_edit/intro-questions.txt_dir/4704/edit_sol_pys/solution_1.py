

n = int(input())
a = list(map(int, input().split()))

s = [0]
for i in range(n):
    s.append(s[i] + a[i])

min_diff = float('inf')
for i in range(1, n):
    diff = abs(s[i] - (s[n] - s[i]))
    min_diff = min(min_diff, diff)

print(min_diff)

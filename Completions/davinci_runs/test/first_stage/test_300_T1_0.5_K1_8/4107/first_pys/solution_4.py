

n, k = map(int, input().split())
s = input()

cost = 0
for i in range(n):
    if s[i] == '1':
        cost += i + 1
        continue
    if i - k > 0 and s[i - k] == '1':
        continue
    if i + k < n and s[i + k] == '1':
        continue
    cost += i + 1

print(cost)
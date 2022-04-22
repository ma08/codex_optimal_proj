
# Solution

n, k = [int(x) for x in input().split()]
s = input()

cost = 0
for i in range(1, n + 1):
    if s[i - 1] == '1':
        cost += i
        continue
    if i - k - 1 >= 0 and s[i - k - 1] == '1':  # prev
        continue
    if i + k - 1 < n and s[i + k - 1] == '1':  # next
        continue
    cost += i

print(cost)

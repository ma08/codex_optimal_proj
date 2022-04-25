

# Solution 1

n, k = [int(x) for x in input().split()]
s = input()

cost = 0
for i in range(1, n + 1):
    if s[i - 1] == '1':
        cost += i
        continue
    if i - k - 1 >= 0 and s[i - k - 1] == '1':
        continue
    if i + k - 1 < n and s[i + k - 1] == '1':
        continue
    cost += i


# Solution 2

n, k = [int(x) for x in input().split()]
s = input()

cost = 0
for i in range(1, n + 1):
    if s[i - 1] == '0':
        cost += i

print(cost)

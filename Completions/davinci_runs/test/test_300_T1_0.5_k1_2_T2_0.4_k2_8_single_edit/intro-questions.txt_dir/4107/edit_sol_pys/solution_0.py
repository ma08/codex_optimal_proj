

# Solution

n, k = [int(x) for x in input().split()]
s = input()

cost = 0
for i in range(n):
    if s[i] == '1':
        continue  # already covered
    if i - k >= 0 and s[i - k] == '1':
        continue  # covered by previous
    if i + k < n and s[i + k] == '1':
        continue  # covered by next
    cost += i + 1  # covered by i+1th

print(cost)

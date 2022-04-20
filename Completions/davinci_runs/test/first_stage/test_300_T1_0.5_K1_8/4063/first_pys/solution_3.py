

n = int(input())
d = [int(i) for i in input().split()]

d.sort()

target = sum(d) // 2

count = 0
for i in range(n):
    if target < d[i]:
        break
    count += 1
    target -= d[i]

print(count)
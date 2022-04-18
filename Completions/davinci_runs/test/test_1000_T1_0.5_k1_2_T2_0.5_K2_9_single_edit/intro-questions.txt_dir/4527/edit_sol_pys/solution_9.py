
# https://www.hackerrank.com/challenges/greedy-florist/problem
# Greedy Algorithm

t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for __ in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1])
    count = 0
    j = 0
    for i in range(n):
        if a[i][0] >= a[j][1]:
            count += 1
            j = i

# https://www.hackerrank.com/challenges/mark-and-toys/problem
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
count = 0
for i in range(n):
    if k - a[i] >= 0:
        k -= a[i]
        count += 1
    else:
        break
print(count)

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem
n = int(input())
a = list(map(int, input().split()))
a.sort()
m = abs(a[0] - a[1])
for i in range(1, n - 1):
    m = min(m, abs(a[i] - a[i + 1]))
print(m)

# https://www.hackerrank.com/challenges/luck-balance/problem
n, k = map(int, input().split())
a = []
for _ in range(n):
    l, t = map(int, input().split())
    a.append([l, t])
a.sort(key=lambda x: x[0])
count = 0
for i in range(n):
    if a[i][1] == 0:
        count += a[i][0]
    else:
        if k > 0:
            count += a[i][0]
            k -= 1
        else:
            count -= a[i][0]
print(count)
    print(count)

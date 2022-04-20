

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k == 1:
    print(0)
    exit()

a.sort()

if a[0] == a[-1]:
    print(0)
    exit()

if k == n:
    print(a[-1] - a[0])
    exit()

d = a[-1] - a[0]

# print(a)

first_min = a[0]
last_max = a[-1]

# print(first_min, last_max)

for i in range(1, n):
    if a[i] > first_min:
        break


# print(i)

for j in range(n-2, -1, -1):
    if a[j] < last_max:
        break


# print(j)

if i == 0 or j == n-1:
    print(d)
    exit()

if i >= k:
    print(d)
    exit()

if j <= n - k:
    print(d)
    exit()

if i + n - j < k:
    print(d)
    exit()

if i + n - j == k:
    print(d - (n - j - i))
    exit()

if i + n - j > k:
    print(d - (i + n - j - k))
    exit()
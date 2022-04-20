

n, w = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

if n == 1:
    print(w + 1)
    exit()

for i in range(1, n):
    a[i] += a[i - 1]

min_a = a[0]
max_a = a[0]

for i in range(1, n):
    if a[i] < min_a:
        min_a = a[i]
    if a[i] > max_a:
        max_a = a[i]

if min_a < 0:
    min_a = -min_a

if max_a > w or min_a > w:
    print(0)
    exit()

if max_a - min_a <= w:
    print(max_a - min_a + 1)
    exit()

if max_a > w:
    print(max_a - w)
    exit()

if min_a > w:
    print(min_a - w)
    exit()
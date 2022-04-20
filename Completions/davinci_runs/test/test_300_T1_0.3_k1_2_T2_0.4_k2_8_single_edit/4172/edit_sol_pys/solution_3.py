
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

min_a = min(a)
max_a = max(a)

if min_a == max_a:
    print(0)
    exit()

if k == 1:
    print(0)
    exit()

if k == n:
    print(max_a - min_a)
    exit()

if k < n:
    if max_a - min_a > 1:
        print(max_a - min_a)
    else:
        print(1)

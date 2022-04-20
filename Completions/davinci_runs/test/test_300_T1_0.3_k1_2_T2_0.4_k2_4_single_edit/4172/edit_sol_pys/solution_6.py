

n, k = [int(x) for x in input().split()]  # n - number of integers in array, k - number of operations
a = [int(x) for x in input().split()]  # array of integers

min_a = min(a)  # minimum integer in array
max_a = max(a)  # maximum integer in array

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

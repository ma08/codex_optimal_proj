

n = int(input())
a = [int(x) for x in input().split()]

min_a = min(a)
max_a = max(a)

if min_a == max_a:
    print(0)
else:
    print(max_a - min_a if max_a % 2 == min_a % 2 else max_a - min_a - 1)


n = int(input())
a = [int(x) for x in input().split()]

min_a = min(a)
max_a = max(a)

if min_a == max_a:
    print('YES')
else:
    print('NO')
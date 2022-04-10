

# SOLUTION

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

if k < n:
    print('NO')
else:
    k = n
    print('YES')
    for i in a:
        print(i, end=' ')
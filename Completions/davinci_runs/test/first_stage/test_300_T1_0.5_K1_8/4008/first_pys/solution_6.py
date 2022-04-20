

n, k = map(int, input().split())
a = list(map(int, input().split()))

# if n < k, then there are at least one color that has no elements
# if n == k, then each color has at least one element
# if n > k, then there are at least two elements of the same color
if n < k:
    print('NO')
else:
    print('YES')
    if n == k:
        for i in a:
            print(i, end=' ')
    else:
        for i in range(n):
            print(i % k + 1, end=' ')
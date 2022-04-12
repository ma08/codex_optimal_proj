def f(n, k):
    if n % 2 == 0:
        return 'YES' if k % 2 == 0 else 'NO'
    else:  # n is odd
        return 'NO' if k % 2 == 0 else 'YES'


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(f(n, k))

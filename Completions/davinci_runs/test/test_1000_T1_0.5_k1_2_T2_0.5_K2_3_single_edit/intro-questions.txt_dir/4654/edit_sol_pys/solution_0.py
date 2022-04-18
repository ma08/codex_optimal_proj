
def f(n, k):
    if n % k == 0:
        return 'YES'
    if k % 2 == 0:
        if n % 2 == 0:
            return 'NO'
        else:
            return 'YES'
    else:
        if n % 2 == 0:
            return 'YES'
        else:
            return 'NO'


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(f(n, k))

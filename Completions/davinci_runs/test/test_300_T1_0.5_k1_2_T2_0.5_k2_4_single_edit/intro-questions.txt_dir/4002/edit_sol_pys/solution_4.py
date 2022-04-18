
def max_sum(n,m,k):
    if k == 1:
        return (n*m)**2
    else:
        if n == 1:
            return (m*(m-1) + m)**2
        elif m == 1:
            return (n*(n-1) + n)**2
        else:
            return (n*(n-1) + n)*(m*(m-1) + m)
for _ in range(int(input())):
    n,m,k = map(int, input().split())
    print(max_sum(n,m,k))

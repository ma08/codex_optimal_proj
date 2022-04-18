
def f(n, k):
    if n % k == 0:
        return True
    if k % 2 == 0:
        if n % 2 == 0:
            return False
        else:
            return True
    else:
        if n % 2 == 0:
            return True
        else:
            return False


def g(n, k):
    if n % k == 0:
        return True
    if n % 2 == 0:
        return False
    else:
        return True


t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(f(n, k))

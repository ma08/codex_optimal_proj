from decimal import Decimal


n, m = map(int, input().split())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

u = list(map(Decimal, input().split()))

t = list(map(Decimal, input().split()))

s = list(map(Decimal, input().split()))

v = list(map(Decimal, input().split()))

def calc_sim(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxx = sum([x[i] ** 2 for i in range(n)])
    syy = sum([y[i] ** 2 for i in range(n)])
    sxy = sum([x[i] * y[i] for i in range(n)])
    return (n * sxy - sx * sy) / (((n * sxx - sx ** 2) * (n * syy - sy ** 2)) ** (1/2))
    
def calc_r(x, y):
    return calc_sim(x, y) * ((len(x) - 2) / (1 - calc_sim(x, y) ** 2)) ** (1/2)

print(calc_r(u, t))
print(calc_r(s, v))

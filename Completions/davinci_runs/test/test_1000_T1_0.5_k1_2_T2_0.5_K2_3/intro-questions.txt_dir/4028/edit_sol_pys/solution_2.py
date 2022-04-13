
n = int(input())
s = input()

def f(n, s, m):
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n in m:
        return m[n]
    m[n] = (f(n-2, s, m) * 3 + f(n-1, s, m) * 2) % 1000000007
    return m[n]

print(f(n, s) % 1000000007)

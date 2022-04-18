

def coconut_splat(s, n, a):
    if s == 9:
        return (n - 1) % 2 + a
    else:
        return (n - 1) % 3 + a

s, n = map(int, input().split())
print(coconut_splat(s, n))



def coconut_splat(s, n):
    if s == 1:
        return 1
    else:
        return (coconut_splat(s - 1, n) + n - 1) % s + 1

print(coconut_splat(10, 3))

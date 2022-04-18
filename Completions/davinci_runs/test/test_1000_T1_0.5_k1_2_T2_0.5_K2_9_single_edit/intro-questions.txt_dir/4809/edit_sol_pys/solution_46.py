
def coconut_splat(s, n):
    return (n - 1) % (s + 1) + 1

s, n = map(int, input().split())
print(coconut_splat(s, n))

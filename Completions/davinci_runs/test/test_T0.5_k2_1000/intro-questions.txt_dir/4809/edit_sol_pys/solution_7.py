
def coconut_split(s, n):
    if s == 9:
        return (n - 1) % 2 + 1
    else:
        return (n - 1) % 3 + 1

s, n = map(int, input().split())
print(coconut_split(s, n))

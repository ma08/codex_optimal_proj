

# Solution
def solve(a, b):
    a.sort()
    b.sort()

    suma = sum(a[::2])
    sumb = sum(a[1::2])

print(suma, sumb)

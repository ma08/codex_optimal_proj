

def rev(n):
    return int(str(n)[::-1])

a, b = input().split()
a = int(a)
b = int(b)

if rev(a) > rev(b):
    print(rev(a))
else:
    print(rev(b))

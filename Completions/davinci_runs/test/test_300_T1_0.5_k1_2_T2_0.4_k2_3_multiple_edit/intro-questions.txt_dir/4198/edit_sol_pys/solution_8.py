
# A, B, X = map(int, input().split())
A, B, X = map(int, input().split())

if A + B > X:
    print(0)
    exit()

k = (X - B) // A
l = len(str(k))

if A * k + B * l <= X:
    print(k)
else:
    print(k - 10 ** (l - 1))

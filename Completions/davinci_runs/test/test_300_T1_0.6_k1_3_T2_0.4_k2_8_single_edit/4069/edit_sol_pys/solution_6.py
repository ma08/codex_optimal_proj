

X, Y = map(int, input().split())

if X > Y:
    print(X - Y)
elif X == Y:
    print(0)
else:
    print(Y - X)

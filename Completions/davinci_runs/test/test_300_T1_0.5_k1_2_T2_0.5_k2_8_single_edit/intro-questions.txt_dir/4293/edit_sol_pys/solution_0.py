
N, A, B = map(int, input().split())
a = N // (A + B)
b = N % (A + B)
if b <= A:
    print(A * a + b)
else:
    print(A * a + A)

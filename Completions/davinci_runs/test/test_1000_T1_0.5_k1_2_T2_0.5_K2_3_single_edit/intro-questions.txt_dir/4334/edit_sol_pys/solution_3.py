


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))


def f(x):
    return x[1] - x[0]


A.sort()
B.sort()
C.sort(key=f)

ans = 0
for b in B:
    a = bisect_left(A, b)
    c = bisect_right(C, b)
    ans += a * (N - c)
print(ans)

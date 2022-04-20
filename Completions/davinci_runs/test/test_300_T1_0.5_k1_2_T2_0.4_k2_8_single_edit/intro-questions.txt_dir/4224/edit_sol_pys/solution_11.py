# input
N = int(input())
A = list(map(int, input().split()))


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# solve
ans = 0
if N == 1:
    while A[0] % 2 == 0:
        A[0] /= 2
        ans += 1
else:
    gcd_num = gcd(A[0], A[1])
    for i in range(2, N):
        gcd_num = gcd(gcd_num, A[i])

    for i in range(N):
        while A[i] % 2 == 0:
            A[i] /= 2
            ans += 1

    for i in range(N):
        while A[i] % gcd_num == 0:
            A[i] /= gcd_num
            ans += 1

print(ans)

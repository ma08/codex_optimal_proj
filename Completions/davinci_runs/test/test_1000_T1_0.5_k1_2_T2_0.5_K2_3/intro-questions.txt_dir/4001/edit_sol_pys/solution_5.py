def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
A = list(map(int, input().split()))
A.sort()
A.pop(0)
A.pop(N - 2)
print(gcd(A[0], A[1]))

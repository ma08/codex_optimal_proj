
N = int(input())
A = list(map(int, input().split()))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

gcd_max = 0

for i in range(N):
    for j in range(N):
        if i != j:
            gcd_tmp = gcd(A[i], A[j])
            if gcd_max < gcd_tmp:
                gcd_max = gcd_tmp

print(gcd_max)

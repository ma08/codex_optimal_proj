

C, K = map(int, input().split())

for i in range(K, 10):
    if C % (10**i) < 5*(10**(i-1)):
        C = C - C % (10**i)
    else:
        C = C - C % (10**i) + 10**i

print(C)
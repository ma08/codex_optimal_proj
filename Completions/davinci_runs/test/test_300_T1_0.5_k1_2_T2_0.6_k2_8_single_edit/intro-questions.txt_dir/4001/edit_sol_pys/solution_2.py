
N = int(input())
divisors = list(map(int, input().split()))
X = 1
Y = 1
for i in range(N):
    if divisors[i] == 1:
        continue
    if divisors[i] == divisors[i + 1]:
        X *= divisors[i]
        i += 1
    else:
        Y *= divisors[i]
print(X, Y)

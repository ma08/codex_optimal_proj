
N = int(input())
X = list(map(int, input().split()))

def median(l):
    l.sort()
    return l[len(l)//2]

for i in range(N):
    X_copy = X[:i] + X[i+1:]
    print(median(X_copy), end=' ')

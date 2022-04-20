

X = int(input())
N = int(input())
p = [int(i) for i in input().split()]

def nearest(X, N, p):
    if N == 0:
        return X
    else:
        ans = p[0]
        for i in range(1, N):
            if abs(X-p[i]) < abs(X-ans):
                ans = p[i]
        return ans

ans = nearest(X, N, p)

print(ans)
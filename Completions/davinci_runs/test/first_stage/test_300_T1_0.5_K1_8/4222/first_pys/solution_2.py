

# input
N, K = map(int, input().split())
A = []
for i in range(K):
    d = int(input())
    A.append(list(map(int, input().split())))

# initialize
victim = [0]*N

# main
for i in range(K):
    for j in range(d):
        victim[A[i][j]-1] += 1

# output
print(victim.count(0))
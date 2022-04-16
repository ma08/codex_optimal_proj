

#import sys
#sys.stdin = open('input.txt')

M, N = map(int, input().split())
T = list(map(int, input().split()))
X = list(map(int, input().split()))
for i in range(len(X)):
    X[i] = X[i] * 1000
# calculate the distance between each two milestones
D = [X[i+1]-X[i] for i in range(N-1)]

# calculate the time between each two milestones in miliseconds
T1 = [T[i+1]-T[i] for i in range(M-1)]
for i in range(len(T1)):
    T1[i] = T1[i] * 1000

# calculate the speed between each two milestones
S = [D[i]/T1[i] for i in range(M-1)]

# calculate the distance between the first milestone you saw and the second milestone you saw
D2 = [S[i]*T[0] for i in range(M-1)]

# sort D2 in increasing order
D2 = sorted(D2)

# remove duplicate values
D2 = list(set(D2))

# print output
print(len(D2))
print(*D2)

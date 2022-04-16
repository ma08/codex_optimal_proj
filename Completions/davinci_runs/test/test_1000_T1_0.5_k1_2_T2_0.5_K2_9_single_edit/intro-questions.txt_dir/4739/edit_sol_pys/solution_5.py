

#import sys
#sys.stdin = open('input.txt')

M, N = map(int, input().split())
T = list(map(int, input().split()))
X = list(map(int, input().split()))

# calculate the distance between each two milestones, and the time between each two milestones
D = [X[i+1]-X[i] for i in range(M-1)]
T2 = [T[i+1]-T[i] for i in range(M-1)]

# calculate the speed between each two milestones, and the distance between the first milestone you saw and the second milestone you saw
S = [D[i]/T2[i] for i in range(M-1)]
D2 = [S[i]*T[0] for i in range(M-1)]

# calculate the distance between the first milestone you saw and the second milestone you saw
D2 = sorted(D2)

# remove duplicate values from D2
D2 = list(set(D2))

# print the number of unique distances and the unique distances
print(len(D2))
print(*D2)

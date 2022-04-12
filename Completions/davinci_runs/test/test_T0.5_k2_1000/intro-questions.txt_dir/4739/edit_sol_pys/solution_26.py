

#import sys
#sys.stdin = open('input.txt')

M, N = map(int, input().split())
T = list(map(int, input().split()))
X = list(map(int, input().split()))

# calculate the distance between each two milestones (D) 
D = [X[i+1]-X[i] for i in range(N-1)]

# calculate the time between each two milestones (T) 
T = [T[i+1]-T[i] for i in range(M-1)]

# calculate the speed between each two milestones (S) 
S = [D[i]/T[i] for i in range(M-1)]

# calculate the distance between the first milestone you saw and the second milestone you saw (D2) 
D2 = [S[i]*T[0] for i in range(M-1)]

# sort D2 in increasing order
D2 = sorted(D2)

# remove duplicate values
D2 = list(set(D2))

# print output
print(len(D2))
print(*D2)

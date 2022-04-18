

import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split()) # M is the number of milestones you saw, N is the total number of milestones.
T = list(map(int, input().split())) # T is the time you saw each milestone.
X = list(map(int, input().split())) # X is the position of each milestone.

# calculate the distance between each two consecutive milestones.
D = [X[i+1]-X[i] for i in range(M-1)]

# calculate the time between each two consecutive milestones.
T = [T[i+1]-T[i] for i in range(M-1)] 

# calculate the speed between each two consecutive milestones.
S = [D[i]/T[i] for i in range(M-1)]

# calculate the distance between the first milestone you saw and the second milestone you saw.
D2 = [S[i]*T[0] for i in range(M-1)]

# sort D2 in ascending order.
D2 = sorted(D2)

# remove duplicate values.
D2 = list(set(D2))

# print output.
print(len(D2))
print(*D2)

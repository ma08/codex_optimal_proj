
#-----input-----
N = int(input())
F = []
for i in range(N):
    F.append([int(j) for j in input().split(" ")])
P = []
for i in range(N):
    P.append([int(j) for j in input().split(" ")])

#-----output-----
print(max([sum([p*f for p, f in zip(p, f)]) for f in zip(*F) for p in P])) 

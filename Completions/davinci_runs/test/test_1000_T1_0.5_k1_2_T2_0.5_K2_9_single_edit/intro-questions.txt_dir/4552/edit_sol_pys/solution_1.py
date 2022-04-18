

#-----Input-----
N = int(input())
F = []
for i in range(N):
    F.append([int(j) for j in input().split(" ")])
P = []
for i in range(N):
    P.append([int(j) for j in input().split(" ")])

#-----Output-----


#-----Input-----
N = int(input())
A = [int(i) for i in input().split(" ")]

#-----Output-----
print(max(A))


#-----Input-----
N = int(input())
A = [int(i) for i in input().split(" ")]

#-----Output-----
print(min(A))


#-----Input-----
N = int(input())
A = [int(i) for i in input().split(" ")]

#-----Output-----
print(sum(A))


#-----Input-----
N = int(input())
A = [int(i) for i in input().split(" ")]

#-----Output-----
print(sum(A)/N)


#-----Input-----
N = int(input())
A = [int(i) for i in input().split(" ")]

#-----Output-----
print(max(A) - min(A))


#-----Input-----
N = int(input())
A = [int(i) for i in input().split(" ")]

#-----Output-----
print(sorted(A))
print(max([sum([p*f for p, f in zip(p, f)]) for f in zip(*F) for p in P]))

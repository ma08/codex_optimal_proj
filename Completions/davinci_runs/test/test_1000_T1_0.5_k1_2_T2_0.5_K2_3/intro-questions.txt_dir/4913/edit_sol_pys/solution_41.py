N = int(input())

A = []
B = []
C = []

for i in range(N):
    temp = input()
    A.append(temp[0])
    B.append(temp[1])
    C.append(temp[2])

strains = ['A', 'B', 'C']

for i in range(3):
    infected_v = 0
    infected_u = 0
    if strains[i] == 'A':
        for j in range(len(A)):
            if A[j] == 'Y':
                infected_v += 1
        for j in range(len(A)):
            if A[j] == 'N':
                infected_u += 1
    elif strains[i] == 'B':
        for j in range(len(B)):
            if B[j] == 'Y':
                infected_v += 1
        for j in range(len(B)):
            if B[j] == 'N':
                infected_u += 1
    elif strains[i] == 'C':
        for j in range(len(C)):
            if C[j] == 'Y':
                infected_v += 1
        for j in range(len(C)):
            if C[j] == 'N':
                infected_u += 1
    if infected_v == 0:
        print("Not Effective")
    else:
        print(100 - (infected_v/N)/(infected_u/N)*100, end = " ")


N = int(input())


#-----main-----

#input parameter
N, Q = map(int, input().split())

#input S
S = input()

#input Li and Ri
Li = []
Ri = []
for i in range(Q):
    Li.append(l-1)
    Ri.append(r-1)

#count AC in each substring
for i in range(Q):
    count = 0
    for j in range(Li[i], Ri[i]):
        if S[j-1:j+1] == 'AC':
            count += 1
    print(count)

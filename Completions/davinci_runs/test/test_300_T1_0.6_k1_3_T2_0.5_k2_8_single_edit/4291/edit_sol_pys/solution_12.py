
#-----main-----

#input parameter
N, Q = map(int, input().split())

#input S
S = input()

#input Li and Ri
Li = []
Ri = []
for i in range(Q):
    l, r = map(int, input().split())
    Li.append(l)
    Ri.append(r)

#count AC in each substring
count = 0
for i in range(Q):
    for j in range(Li[i]-1, Ri[i]):
        if S[j-1:j+1] == 'AC':
            count += 1
    print(count)
    count = 0

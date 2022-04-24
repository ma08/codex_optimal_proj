

#-----main-----

#input parameter
N, Q = map(int, input().split())

#input S and Li and Ri
S = list(input())
L = []
R = []
for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

#count AC in each substring
count = 0
for i in range(len(L)):
    for j in range(L[i], R[i]):
        if S[j-1:j+1] == 'AC':
            count += 1
    print(count)
    count = 0

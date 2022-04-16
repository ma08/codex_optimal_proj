

N,A = map(int,input().split())
E = list(map(int,input().split()))

E.sort()

#print(E)

i = 0
j = N-1

res = 0

while i <= j:
    if E[i] >= E[j]:
        if A >= E[i]:
            A -= E[i]
            E[i] = 0
            i += 1
        else:
            break
    else:
        if A >= E[j]:
            A -= E[j]
            E[j] = 0
            j -= 1
        else:
            break

#print(E)

for i in range(N):
    if E[i] == 0:
        res += 1

print(res)

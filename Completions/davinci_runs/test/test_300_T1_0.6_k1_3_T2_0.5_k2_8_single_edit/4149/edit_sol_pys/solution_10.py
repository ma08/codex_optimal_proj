

n = int(input())
b = [int(x) for x in input().split()]

a = []

for i in range(n):
    if b[i] in b[n:]: # if number in the first half is in the second half
        a.append(b[i])
    else: # if number in the first half is not in the second half
        for j in range(n, 2*n):
            if b[j] == b[i]:
                a.append(b[j])
                break

print(*a)

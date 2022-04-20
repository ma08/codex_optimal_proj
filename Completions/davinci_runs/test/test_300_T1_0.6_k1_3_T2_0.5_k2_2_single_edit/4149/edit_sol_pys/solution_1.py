

n = int(input())
b = [int(x) for x in input().split()]

a = []

for i in range(n):
    if b[i] in b[n:]: #if element is in the second part of the list
        a.append(b[i]) #append it to the new list
    else:
        for j in range(n, 2*n): #else look for it in the second part
            if b[j] == b[i]: #if it is there
                a.append(b[j]) #append it to the new list
                break

print(*a)

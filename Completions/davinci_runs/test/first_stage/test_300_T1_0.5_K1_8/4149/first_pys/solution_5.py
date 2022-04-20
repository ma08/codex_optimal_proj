

n = int(input())
b = input().split(' ')
b = [int(i) for i in b]

#print(b)

a = []

for i in range(n):
    if b[i] in b[n:]:
        a.append(b[i])
    else:
        a.append(b[n+i])

print(' '.join([str(i) for i in a]))


#input
n = int(input())
a = [int(x) for x in input().split()]

#solution
b = []
for i in range(n-1,-1,-1):
    if a[i] not in b:
        b.append(a[i])

#output
print(len(b))
print(' '.join([str(x) for x in b[::-1]]))
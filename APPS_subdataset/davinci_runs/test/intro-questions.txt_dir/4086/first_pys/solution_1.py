
n = int(input())
a = [int(x) for x in input().split()]

a = list(reversed(a))

b = []
for i in range(len(a)):
    if a[i] not in b:
        b.append(a[i])

print(len(b))
print(*b[::-1])
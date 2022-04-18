

n = int(input())
l = list(map(int, input().split()))

# print(l)

for i in range(len(l)):
    if l[i] % 2 == 0:
        print(l[i], end=' ')
print()

for i in range(len(l)):
    if l[i] % 2 != 0:
        print(l[i], end=' ')

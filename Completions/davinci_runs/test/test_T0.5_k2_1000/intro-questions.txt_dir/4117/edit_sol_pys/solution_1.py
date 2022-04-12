
n = int(input())
l = sorted(list(map(int, input().split())))

print(l)

for i in range(n):
    for j in range(n):
        if l[i] + l[j] == l[i] + l[j]:
            print(l[i], l[j])

n = int(input())
l = list(map(int, input().split()))

# print(l)

s = 0
for i in range(len(l)):
    for j in range(i + 1, len(l)):
        # print(l[i], l[j])
        if l[i] == l[j]:
            s += 1

print(s)

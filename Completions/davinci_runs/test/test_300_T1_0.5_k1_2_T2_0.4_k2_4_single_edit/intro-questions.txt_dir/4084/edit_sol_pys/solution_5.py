

n = int(input())
b = [int(input()) for i in range(n)]
s = 0
for i in range(n):
    for j in range(n):
        if b[i] == b[j]:
            s += 1
print(s)


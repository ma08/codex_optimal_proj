

n = int(input())
f = list(map(int, input().split()))
 
if f.count(0) == 1:
    for i in range(n):
        if f[i] == 0:
            for j in range(n):
                if f[j] != 0:
                    f[i] = j + 1
                    break
else:
    for i in range(n):
        if f[i] == 0:
            for j in range(n):
                if f[j] == 0:
                    f[i] = j + 1
                    f[j] = i + 1
                    break

print(*f)


N = int(input())

# 素数を数える
c = [0 for i in range(N+1)]

for i in range(2, N+1):
    if c[i] == 0:
        for j in range(i, N+1, i):
            c[j] += 1

print(c.count(8))



n = int(input())
f = [int(x) for x in input().split()]

gifts = [0] * n
presents = [0] * n

for i in range(n):
    if f[i] != 0:
        gifts[f[i]-1] += 1
        presents[i] = f[i]

for i in range(n):
    if presents[i] == 0:
        for j in range(n):
            if gifts[j] == 0:
                presents[i] = j+1
                gifts[j] += 1
                break

print(' '.join([str(x) for x in presents]))
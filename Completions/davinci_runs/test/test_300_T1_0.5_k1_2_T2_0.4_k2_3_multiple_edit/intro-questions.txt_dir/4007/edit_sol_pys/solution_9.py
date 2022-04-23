

n = int(input())
f = [int(x) for x in input().split()]

# Find friends who don't know who to give gifts to
no_gift_to = []
for i in range(n):
    if f[i] == 0:
        no_gift_to.append(i)

# Give gifts to friends who don't know who to give gifts to
    for j in range(n):
        if f[j] == 0:
            f[j] = no_gift_to[i] + 1
            break

print(" ".join(str(x) for x in f))



n = int(input())
f = [int(x) for x in input().split()]

# Find friends who don't know who to give gifts to
# and friends who don't know who gives them gifts
no_gift_to = []
no_gift_from = []
for i in range(n):
    if f[i] == 0:  # if friend i doesn't know who to give gifts to
        no_gift_to.append(i)
    else:  # if friend i knows who to give gifts to
        if f[f[i] - 1] == 0:  # if friend i's gift receiver doesn't know who gives him gifts
            no_gift_from.append(f[i] - 1)

# Give gifts to friends who don't know who gives them gifts
for i in range(len(no_gift_to)):
    f[no_gift_from[i]] = no_gift_to[i] + 1

# Give gifts to friends who don't know who to give gifts to
for i in range(len(no_gift_to)):
    f[no_gift_to[i]] = no_gift_from[i] + 1

print(" ".join(str(x) for x in f))



n = int(input())
f = list(map(int, input().split()))

# For each friend i, we want to know the friend j whom i wants to give a gift to
# So we create a dictionary that maps i to j
# We also keep track of the number of friends who want to give a gift to each friend
# Each friend i should have 1 outgoing gift and 1 incoming gift
# If a friend i has 0 outgoing gifts, we give him an outgoing gift to the friend who has the most incoming gifts
# If a friend i has 2 outgoing gifts, we take one of the outgoing gifts away
# If a friend i has 1 outgoing gift and 1 incoming gift, we do nothing
# We keep doing this until no friend has 2 outgoing gifts

gifts = dict()
incoming = dict()
outgoing = dict()

for i in range(n):
    if f[i] != 0:
        gifts[i] = f[i] - 1
        if f[i] - 1 in incoming:
            incoming[f[i] - 1] += 1
        else:
            incoming[f[i] - 1] = 1
        if i in outgoing:
            outgoing[i] += 1
        else:
            outgoing[i] = 1

while any(map(lambda x: x >= 2, outgoing.values())):
    for i in range(n):
        if i in outgoing:
            if outgoing[i] >= 2:
                del gifts[i]
                outgoing[i] -= 1
                incoming[gifts[i]] -= 1
            elif outgoing[i] == 1 and i not in incoming:
                most_incoming = max(incoming, key=incoming.get)
                incoming[most_incoming] += 1
                outgoing[i] += 1
                gifts[i] = most_incoming

for i in range(n):
    if i not in outgoing:
        print(1, end=' ')
    else:
        print(gifts[i] + 1, end=' ')
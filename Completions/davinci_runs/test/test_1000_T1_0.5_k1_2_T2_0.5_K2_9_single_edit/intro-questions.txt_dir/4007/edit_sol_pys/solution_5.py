
n = int(input())
f = [int(x) for x in input().split()]  # list of friends

# Find friends who don't know who to give gifts to and friends who don't know who gives them gifts
no_gift_to = []
no_gift_from = []

for i in range(n):  # for each friend
    if f[i] == 0:  # if friend does not know who to give gift to
        no_gift_to.append(i)  # add friend to list of friends who don't know who to give gifts to
    else:
        if f[f[i] - 1] == 0:  # if friend's friend does not know who gives them gift
            no_gift_from.append(f[i] - 1)  # add friend's friend to list of friends who don't know who gives them gifts

# Give gifts to friends who don't know who gives them gifts
for i in range(len(no_gift_to)):  # for each friend who doesn't know who to give gifts to
    f[no_gift_from[i]] = no_gift_to[i] + 1  # give gift to friend's friend

# Give gifts to friends who don't know who to give gifts to
for i in range(len(no_gift_to)):  # for each friend who doesn't know who to give gifts to
    f[no_gift_to[i]] = no_gift_from[i] + 1  # give gift to friend

print(" ".join(str(x) for x in f))  # print answer

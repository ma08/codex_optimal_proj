

n = int(input())
f = [int(x) for x in input().split()]

def find_gift_to(f, n):
    # Find friends who don't know who to give gifts to
    # and friends who don't know who gives them a gift
    no_gift_to = []
    no_gift_from = []
    for i in range(n):
        if f[i] == 0:
            no_gift_to.append(i)
        else:
            if f[f[i] - 1] == 0:
                no_gift_from.append(f[i] - 1)

    # Give gifts to friends who don't know who gives them a gift
    for i in range(len(no_gift_to)):
        f[no_gift_from[i]] = no_gift_to[i] + 1

    # Give gifts to friends who don't know who to give a gift to
    for i in range(len(no_gift_to)):
        f[no_gift_to[i]] = no_gift_from[i] + 1

    print(" ".join(str(x) for x in f))

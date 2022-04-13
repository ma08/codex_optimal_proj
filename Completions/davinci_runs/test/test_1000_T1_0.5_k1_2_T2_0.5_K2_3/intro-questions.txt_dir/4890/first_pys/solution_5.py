

def solve(n, m, s, d, c):
    if sum(c) + n < m:
        return "impossible"

    # create a list of tuples (c,d) representing the capacities of each slot
    slots = zip(c, [d]*s)
    # sort the list of slots by capacity, descending
    slots = sorted(slots, key=lambda x: x[0], reverse=True)

    # create a list of tuples (c,d) representing the number of bottles to add to each slot
    add = [(0,0)]*s

    # add bottles to the slots with the most free space
    for i in range(n):
        # find the slot with the most free space
        slot = max(slots, key=lambda x: x[1]-x[0])
        # add a bottle to the slot
        add[slots.index(slot)] = (add[slots.index(slot)][0]+1, add[slots.index(slot)][1])
        # update the slot's capacity
        slot = (slot[0]+1, slot[1])
        slots[slots.index(slot)] = slot

    # sort the list of bottles to add to each slot by the number of bottles in each slot, descending
    add = sorted(add, key=lambda x: x[0], reverse=True)

    # create a list of tuples (c,d) representing the updated capacities of each slot
    slots = [(x[0]+y[0], x[1]) for x, y in zip(c, add)]
    # sort the list of slots by capacity, descending
    slots = sorted(slots, key=lambda x: x[0], reverse=True)

    # create a list of tuples (c,d) representing the probability of getting a cold bottle from each slot
    p = [(x[0]/float(x[1]), x[1]) for x in slots]
    # sort the list of probabilities by probability, descending
    p = sorted(p, key=lambda x: x[0], reverse=True)

    # calculate the probability that the next m students get a cold bottle
    prob = 1.0
    for i in range(m):
        prob *= p[i][0]

    # if the probability is 0, return "impossible"
    if prob == 0:
        return "impossible"

    # otherwise, return the list of bottles to add to each slot
    return [x[0] for x in add]

if __name__ == "__main__":
    n, m, s, d = map(int, raw_input().split())
    c = map(int, raw_input().split())
    print " ".join(map(str, solve(n, m, s, d, c)))


n, k = [int(i) for i in input().split()]
s = input()

# This is the solution I came up with on my own.
# It's very slow and I haven't been able to figure out why.
# It's a greedy algorithm that adds routers to the first available spot.
# The algorithm starts at the beginning of the string and adds a router
# to the first available spot. Then it moves to the next spot that is not
# already covered by the first router and adds a router there. It continues
# until all rooms are covered.

# def get_next_router_spot(s, start=0):
#     for i in range(start, len(s)):
#         if s[i] == "1":
#             return i
#     return None

# routers = []
# while True:
#     router = get_next_router_spot(s)
#     if router is None:
#         break
#     routers.append(router)
#     for i in range(router - k, router + k + 1):
#         if i >= 0 and i < len(s):
#             s = s[:i] + "0" + s[i+1:]

# print(sum(routers))

# This is the solution I found online.
# It's much faster than my solution.
# It's a greedy algorithm that adds routers to the highest available spot.
# It starts by adding routers to the highest available spot, then it moves
# to the next highest available spot, etc.

# This is a greedy algorithm. We will always place a router in the highest
# available spot.

# First, we need to find the highest available spot.
highest_spot = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == "1":
        highest_spot = i
        break

# Now we start adding routers.
routers = []
while highest_spot >= 0:
    routers.append(highest_spot)
    # We need to remove all spots that are covered by this router.
    for i in range(highest_spot - k, highest_spot + k + 1):
        if i >= 0 and i < len(s):
            s = s[:i] + "0" + s[i+1:]
    # Now we need to find the next highest available spot.
    highest_spot = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            highest_spot = i
            break

print(sum(routers))
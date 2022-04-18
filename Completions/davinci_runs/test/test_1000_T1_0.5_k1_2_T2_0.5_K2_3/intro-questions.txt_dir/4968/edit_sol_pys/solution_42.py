

# Get input
N, S, R = [int(x) for x in input().split()]
dmg = [int(x) for x in input().split()]
rsv = [int(x) for x in input().split()]

# Find the number of teams that can't start
# Start with the number of teams with damaged kayaks
# Subtract the number of teams with reserve canoes
# Add the number of teams that can be helped by reserve canoes
# Subtract the number of teams that are helped by reserve canoes
#   but are not next to the team with the reserve canoe
# Subtract the number of teams that are helped by a reserve canoe
#   but are not next to any team with a damaged kayak
# Subtract the number of teams that are helped by a reserve canoe
#   but are not next to any other team with a reserve canoe
# Add the number of teams that are helped by a reserve canoe
#   and are next to a team with a damaged canoe
# Add the number of teams that are helped by a reserve canoe
#   and are next to another team with a reserve canoe
# Add the number of teams that are helped by a reserve canoe
#   and are next to a team with a damaged canoe and a team with a reserve canoe
cantStart = S - R
cantStart -= sum([1 for x in dmg if x - 1 not in rsv and x + 1 not in rsv])
cantStart -= sum([1 for x in rsv if x - 1 not in dmg and x + 1 not in dmg])
cantStart -= sum([1 for x in rsv if x - 1 not in rsv and x + 1 not in rsv])
cantStart += sum([1 for x in dmg if x - 1 in rsv or x + 1 in rsv])
cantStart += sum([1 for x in rsv if x - 1 in rsv or x + 1 in rsv])
cantStart += sum([1 for x in dmg if (x - 1 in rsv or x + 1 in rsv) and (x - 1 in dmg or x + 1 in dmg)])

# Print the result
print(cantStart)



# Get input
N, S, R = [int(x) for x in input().split()]
damaged = [int(x) for x in input().split()]
reserve = [int(x) for x in input().split()]

# Find the number of teams that can't start
# Start with the number of teams with damaged kayaks
# Subtract the number of teams with reserve kayaks
# Add the number of teams that can be helped by reserve kayaks
# Subtract the number of teams that are helped by reserve kayaks
#   but are not next to the team with the reserve kayak
# Subtract the number of teams that are helped by a reserve kayak
#   but are not next to any team with a damaged kayak
# Subtract the number of teams that are helped by a reserve kayak
#   but are not next to any other team with a reserve kayak
# Add the number of teams that are helped by a reserve kayak
#   and are next to a team with a damaged kayak
# Add the number of teams that are helped by a reserve kayak
#   and are next to another team with a reserve kayak
# Add the number of teams that are helped by a reserve kayak
#   and are next to a team with a damaged kayak and a team with a reserve kayak
cantStart = S - R
cantStart -= sum([1 for x in damaged if x - 1 not in reserve and x + 1 not in reserve])
cantStart -= sum([1 for x in reserve if x - 1 not in damaged and x + 1 not in damaged])
cantStart -= sum([1 for x in reserve if x - 1 not in reserve and x + 1 not in reserve])
cantStart += sum([1 for x in damaged if x - 1 in reserve or x + 1 in reserve])
cantStart += sum([1 for x in reserve if x - 1 in reserve or x + 1 in reserve])
cantStart += sum([1 for x in damaged if (x - 1 in reserve and x + 1 in reserve) or (x - 1 in reserve and x + 1 in reserve)])

# Print the result
print(cantStart)

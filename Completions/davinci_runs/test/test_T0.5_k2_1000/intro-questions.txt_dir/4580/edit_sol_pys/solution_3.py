
n = int(input())
ratings = [int(i) for i in input().split()]
# The minimum possible number of different flavours
min_flavour = 0
for rating in ratings:
    if rating <= 3200:
        min_flavour += 1
    else:
        min_flavour += 2
print(min_flavour)

# The maximum possible number of different flavours
max_flavour = len(set(ratings))
print(max_flavour)

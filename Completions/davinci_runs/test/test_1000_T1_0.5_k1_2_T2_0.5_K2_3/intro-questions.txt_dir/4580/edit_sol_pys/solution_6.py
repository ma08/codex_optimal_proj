
n = int(input())
ratings = [int(i) for i in input().split()]

# The minimum possible number of different colors
min_colors = 0
for rating in ratings:
    if rating <= 3200:
        min_colors += 1
    else:
        min_colors += 2
print(min_colors)

# The maximum possible number of different colors
max_colors = len(set(ratings))
print(max_colors)

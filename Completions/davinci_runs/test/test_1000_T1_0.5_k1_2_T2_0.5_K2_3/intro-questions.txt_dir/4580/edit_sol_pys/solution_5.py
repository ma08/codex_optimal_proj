# The minimum possible number of different colors

n = int(input())
ratings = [int(i) for i in input().split()]
min_color = 0
for rating in ratings:
    if rating <= 3200:
        min_color += 1
    else:
        min_color += 2
print(min_color)  # The minimum possible number of different colors

# The maximum possible number of different colors.
max_color = len(set(ratings))
print(max_color)  # The maximum possible number of different colors.

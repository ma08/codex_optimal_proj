

n = int(input())  # number of ratings
ratings = [int(i) for i in input().split()]

# The minimum possible number of different colors in the given ratings
min_color = 0
for rating in ratings:
    if rating <= 3200:
        min_color += 1
    else:
        min_color += 2
print(min_color)

# The maximum possible number of different colors in the given ratings
max_color = len(set(ratings))
print(max_color)

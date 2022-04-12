n = int(input())
ratings = [int(i) for i in input().split()]  # The list of ratings

# The minimum possible number of different colors (at least two colors)
min_color = len(set(ratings))
if min_color < 2:
    min_color = 2
print(min_color, end=' ')

# The maximum possible number of different colors
max_color = len(set(ratings))
print(max_color, end=' ')

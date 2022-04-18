
n = int(input())
ratings = [int(i) for i in input().split()]

# The minimum possible number of different ratings
min_rating = 0
for rating in ratings:
    if rating <= 3200:
        min_rating += 1
    else:
        min_rating += 2
print(min_rating)

# The maximum possible number of different ratings
max_rating = len(set(ratings))
print(max_rating)

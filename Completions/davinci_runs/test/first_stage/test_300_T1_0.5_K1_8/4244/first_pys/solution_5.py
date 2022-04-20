

num_people = int(input())
positions = list(map(int, input().split()))

# sum(positions) / len(positions) is the mean of all the positions
# The meeting can only be held at an integer coordinate, so floor(mean) is the meeting point
min_stamina = sum([(position - floor(sum(positions) / len(positions))) ** 2 for position in positions])
print(min_stamina)
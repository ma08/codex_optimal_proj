

n = int(input())
a = list(map(int, input().split()))

# sort the array and create a dictionary of the number of elements at each skill level
a.sort()
counts = {}
for num in a:
    if num not in counts:
        counts[num] = 1
    else:
        counts[num] += 1

# iterate through the skill levels and find the highest number of elements that could be in a team
max_count = 0
for skill in counts:
    count = 0
    for sub_skill in range(skill - 5, skill + 6):
        if sub_skill in counts:
            count += counts[sub_skill]
    max_count = max(max_count, count)

print(max_count)
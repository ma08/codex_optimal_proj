

from collections import defaultdict


N = int(input())

# Create a list of the possible temperatures
temp_list = []
for i in range(N):
    temp_list.append(list(map(int, input().split())))


# Create a dictionary of the possible temperatures
temp_dict = defaultdict(list)
for i in range(N):
    temp_dict[temp_list[i][0]].append(temp_list[i][1])


sorted_dict = sorted(temp_dict.items())

# Find the maximum number of rooms required
max_rooms = 0
for i in range(N):
    temp_rooms = 1
    for j in range(i+1, N):
        if sorted_dict[j][0] <= sorted_dict[i][1]:
            temp_rooms += 1
        else:
            break
    if temp_rooms > max_rooms:
        max_rooms = temp_rooms

# Print the result
print(max_rooms)

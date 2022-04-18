

# from collections import defaultdict
#
# N = int(input())
#
# # Create a list of the possible temperatures
# temp_list = []
# for i in range(N):
#     temp_list.append(list(map(int, input().split())))
#
# # Create a dictionary of the possible temperatures
# temp_dict = defaultdict(list)
# for i in range(N):
#     temp_dict[temp_list[i][0]].append(temp_list[i][1])
#
# # Sort the dictionary
# sorted_dict = sorted(temp_dict.items())
#
# # Find the maximum number of rooms required
# max_rooms = 0
# for i in range(N):
#     temp_rooms = 1
#     for j in range(i+1, N):
#         if sorted_dict[j][0] <= sorted_dict[i][1]:
#             temp_rooms += 1
#         else:
#             break
#     if temp_rooms > max_rooms:
#         max_rooms = temp_rooms
#
# print(max_rooms)


# from collections import defaultdict
#
# N = int(input())
#
# # Create a list of the possible temperatures
# temp_list = []
# for i in range(N):
#     temp_list.append(list(map(int, input().split())))
#
# # Create a dictionary of the possible temperatures
# temp_dict = defaultdict(list)
# for i in range(N):
#     temp_dict[temp_list[i][0]].append(temp_list[i][1])
#
# # Sort the dictionary
# sorted_dict = sorted(temp_dict.items())
#
# # Find the maximum number of rooms required
# max_rooms = 1
# curr_rooms = 1
# for i in range(1, N):
#     if sorted_dict[i][0] <= sorted_dict[i-1][1]:
#         curr_rooms += 1
#     else:
#         curr_rooms = 1
#     if curr_rooms > max_rooms:
#         max_rooms = curr_rooms
#
# print(max_rooms)


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

# Sort the dictionary
sorted_dict = sorted(temp_dict.items())

# Find the maximum number of rooms required
max_rooms = 1
curr_rooms = 1
for i in range(1, N):
    if sorted_dict[i][0] <= sorted_dict[i-1][1]:
        curr_rooms += 1
    else:
        curr_rooms = 1
    if curr_rooms > max_rooms:
        max_rooms = curr_rooms

print(max_rooms)





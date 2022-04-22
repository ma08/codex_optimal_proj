

N, K = map(int, input().split())
A = list(map(int, input().split()))

# Make a list storing the number of the people in each team
team_number_list = [0] * N
# Make a list storing the number of the teams
team_list = [0] * N
# Initialize the number of the team to 1
team_number = 1

# Iterate through all the people
for i in range(N):
    # If the person does not belong to any team
    if team_number_list[i] == 0:
        # Add the person to the team with the team number
        team_number_list[i] = team_number
        # Add the person to the list
        team_list[i] = 1
        # Increment the team number by 1
        team_number += 1

    # If the person belongs to the team
    else:
        # Iterate through the list
        for j in range(N):
            # If the person is in the list
            if A[i] == A[j]:
                # If the person does not belong to any team
                if team_number_list[i] == 0:
                    # Add the person to the same team with the person
                    team_number_list[i] = team_number_list[j]
                    # Increment the number of the people in the team by 1
                    team_list[team_number_list[j]] += 1

# print(team_number_list)
# print(team_list)

# Make a list storing the number of the people in the teams
team_number_list2 = [0] * (team_number - 1)

# Iterate through all the people
for i in range(N):
    # Add the number of the people in the team to the list
    team_number_list2[team_number_list[i] - 1] += 1

# print(team_number_list2)

# Initialize the number of the teams to 0
count = 0
# Iterate through all the teams
for i in range(team_number - 1):
    # If the number of the people in the team is more than or equal to K
    if team_number_list2[i] >= K:
        # Increment the number of the teams by 1
        count += 1

print(count)

# print(A)

# for i in range(N):
#     for j in range(A[i][0]):
#         print(A[i][j + 1], end=' ')
#     print()

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# # print(A)
#
# # Make a list storing the number of the people in each team
# team_number_list = [0] * N
# # Make a list storing the number of the teams
# team_list = [0] * N
# # Initialize the number of the team to 1
# team_number = 1
#
# # Iterate through all the people
# for i in range(N):
#     # If the person does not belong to any team
#     if team_number_list[i] == 0:
#         # Add the person to the team with the team number
#         team_number_list[i] = team_number
#         # Add the person to the list
#         team_list[i] = 1
#         # Increment the team number by 1
#         team_number += 1
#
#     # If the person belongs to the team
#     else:
#         # Iterate through the list
#         for j in range(N):
#             # If the person is in the list
#             if A[i] == A[j]:
#                 # If the person does not belong to any team
#                 if team_number_list[i] == 0:
#                     # Add the person to the same team with the person
#                     team_number_list[i] = team_number_list[j]
#                     # Increment the number of the people in the team by 1
#                     team_list[team_number_list[j]] += 1
#
# # print(team_number_list)
# # print(team_list)
#
# # Make a list storing the number of the people in the teams
# team_number_list2 = [0] * (team_number - 1)
#
# # Iterate through all the people
# for i in range(N):
#     # Add the number of the people in the team to the list
#     team_number_list2[team_number_list[i] - 1] += 1
#
# # print(team_number_list2)
#
# # Initialize the number of the teams to 0
# count = 0
# # Iterate through all the teams
# for i in range(team_number - 1):
#     # If the number of the people in the team is more than or equal to K
#     if team_number_list2[i] >= K:
#         # Increment the number of the teams by 1
#         count += 1
#
# print(count)

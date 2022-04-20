

# # Get input
# S = input()
# T = input()

# # Set up variables
# slen = len(S)
# tlen = len(T)

# # Initialize array to store the minimum number of changes needed
# changes = [[0 for i in range(slen + 1)] for j in range(tlen + 1)]

# # Populate the first row
# for i in range(1, slen + 1):
#     changes[0][i] = i

# # Populate the first column
# for j in range(1, tlen + 1):
#     changes[j][0] = j

# # Calculate the rest of the matrix
# for j in range(1, tlen + 1):
#     for i in range(1, slen + 1):
#         if S[i-1] == T[j-1]:
#             changes[j][i] = changes[j-1][i-1]
#         else:
#             changes[j][i] = min(changes[j-1][i], changes[j][i-1], changes[j-1][i-1]) + 1

# print(changes[tlen][slen])

# def get_change(M):
#     coins = [1, 3, 4]
#     min_num_coins = [0] * (M + 1)

#     for m in range(1, M + 1):
#         min_num_coins[m] = float('inf')
#         for i in range(len(coins)):
#             if m >= coins[i]:
#                 num_coins = min_num_coins[m - coins[i]] + 1
#                 if num_coins < min_num_coins[m]:
#                     min_num_coins[m] = num_coins

#     return min_num_coins[M]

# print(get_change(34))

def get_change(M):
    coins = [1, 3, 4]
    min_num_coins = [0] * (M + 1)

    for m in range(1, M + 1):
        min_num_coins[m] = float('inf')
        for i in range(len(coins)):
            if m >= coins[i]:
                num_coins = min_num_coins[m - coins[i]] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[M]

print(get_change(34))

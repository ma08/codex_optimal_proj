

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

# def get_change(m):
#     #write your code here
#     num_coins = 0
#     denom = [10, 5, 1]
#     for i in denom:
#         num_coins += m // i
#         m %= i
#     return num_coins

# if __name__ == '__main__':
#     m = int(input())
#     print(get_change(m))

# def get_change(m):
#     #write your code here
#     num_coins = 0
#     denom = [10, 5, 1]
#     for i in denom:
#         num_coins += m // i
#         m %= i
#     return num_coins

# if __name__ == '__main__':
#     m = int(input())
#     print(get_change(m))

# def get_optimal_value(capacity, weights, values):
#     value = 0.
#     for i in range(len(weights)):
#         if capacity == 0:
#             return value
#         a = min(weights[i], capacity)
#         value += a * values[i] / weights[i]
#         weights[i] -= a
#         capacity -= a
#     return value


# if __name__ == "__main__":
#     data = list(map(int, input().split()))
#     n, capacity = data[0:2]
#     values = []
#     weights = []
#     for i in range(n):
#         data = list(map(int, input().split()))
#         values.append(data[0])
#         weights.append(data[1])
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))

# def get_optimal_value(capacity, weights, values):
#     value = 0.
#     for i in range(len(weights)):
#         if capacity == 0:
#             return value
#         a = min(weights[i], capacity)
#         value += a * values[i] / weights[i]
#         weights[i] -= a
#         capacity -= a
#     return value


# if __name__ == "__main__":
#     data = list(map(int, input().split()))
#     n, capacity = data[0:2]
#     values = []
#     weights = []
#     for i in range(n):
#         data = list(map(int, input().split()))
#         values.append(data[0])
#         weights.append(data[1])
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))

# def get_optimal_value(capacity, weights, values):
#     value = 0.
#     for i in range(len(weights)):
#         if capacity == 0:
#             return value
#         a = min(weights[i], capacity)
#         value += a * values[i] / weights[i]
#         weights[i] -= a
#         capacity -= a
#     return value


# if __name__ == "__main__":
#     data = list(map(int, input().split()))
#     n, capacity = data[0:2]
#     values = []
#     weights = []
#     for i in range(n):
#         data = list(map(int, input().split()))
#         values.append(data[0])
#         weights.append(data[1])
#     opt_value = get_optimal_value(capacity, weights, values)
#     print("{:.10f}".format(opt_value))

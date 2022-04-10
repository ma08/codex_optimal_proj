

n = int(input())
x = [int(i) for i in input().split()]

# calculate the minimum and maximum values of the chips
m = min(x)
M = max(x)

# find the number of chips with the minimum value
m_count = x.count(m)

# find the number of chips with the maximum value
M_count = x.count(M)

# find the number of chips with values between the minimum and maximum values
between_count = n - m_count - M_count

# find the best case for the number of coins to move the chips
best_case = M_count*(M-m) + between_count*(M-m-1)

# print the best case for the number of coins to move the chips
print(best_case)
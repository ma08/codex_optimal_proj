

n = int(input())
k = int(input())

# Number of operations A + Number of operations B = n (1)
# Number of operations A * 2 + Number of operations B * k = minimum value (2)
# Number of operations A * 2 = n - Number of operations B (3)
# Number of operations A = (n - Number of operations B) / 2 (4)
# Number of operations B = n - (n - Number of operations B) / 2 (6)
# Number of operations B = n - n / 2 + Number of operations B / 2 (7)
# Number of operations B = n / 2 + Number of operations B / 2 (8)
# Number of operations B / 2 = n / 2 (9)
# Number of operations B = n (10)
# Number of operations A = n - Number of operations B (11)
# Number of operations A = n - n (12)
# Number of operations A = 0 (13)
# Number of operations B = n (14)
# minimum value = Number of operations B * k (15)
minimum_value = n * k
print(minimum_value)

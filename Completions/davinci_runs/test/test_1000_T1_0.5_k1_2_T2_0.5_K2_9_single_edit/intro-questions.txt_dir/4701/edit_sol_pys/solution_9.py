

n = int(input())
k = int(input())

# Number of operations A + Number of operations B = n
# Number of operations A * 2 + Number of operations B * k = minimum value
# Number of operations A * 2 = n - Number of operations B
# Number of operations A = (n - Number of operations B) / 2
# Number of operations B = n - (n - Number of operations B) / 2
# Number of operations B = n - n / 2 + Number of operations B / 2
# Number of operations B = n / 2 + Number of operations B / 2
# Number of operations B / 2 = n / 2
# Number of operations B = n
# Number of operations A = n - Number of operations B
# Number of operations A = n - n
# Number of operations A = 0
# Number of operations B = n
# minimum value = Number of operations B * k
minimum_value = n * k
print(minimum_value)



n = int(input())
k = int(input())

# Number of operations A + Number of operations B = n => Number of operations B = n - Number of operations A
# Number of operations A * 2 + Number of operations B * k = minimum value => Number of operations B * k = minimum value - Number of operations A * 2
# Number of operations B = n - Number of operations A => Number of operations B * k = minimum value - Number of operations A * 2 => n - Number of operations A * k = minimum value - Number of operations A * 2
# Number of operations A * 2 = n - Number of operations B * k => Number of operations A * 2 = n - minimum value + Number of operations A * 2 => Number of operations A * 2 = n - minimum value => Number of operations A = (n - minimum value) / 2
# Number of operations B = n - Number of operations A => Number of operations B = n - (n - minimum value) / 2 => Number of operations B = minimum value / 2
# minimum value = Number of operations B * k => minimum value = minimum value / 2 * k => minimum value = minimum value * k / 2
# minimum value = n * k / 2
minimum_value = n * k
print(minimum_value)

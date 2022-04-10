

# In: integer
# Out: nearest greater or equal interesting number

a = int(input())

sum_digits = 0

for digit in str(a):
    sum_digits += int(digit)

sum_digits = sum_digits % 4

if sum_digits:
    a = a - sum_digits + 4

print(a)
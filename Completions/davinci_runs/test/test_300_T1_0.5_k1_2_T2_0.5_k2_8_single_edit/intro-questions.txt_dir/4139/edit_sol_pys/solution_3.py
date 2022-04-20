
n = int(input())

# Count the number of 7, 5, and 3 in the number
def count(num):
    count_7 = 0
    count_5 = 0
    count_3 = 0
    for digit in str(num):
        if digit == '7':
            count_7 += 1
        elif digit == '5':
            count_5 += 1
        elif digit == '3':
            count_3 += 1
    return count_7, count_5, count_3

# Check if the number is a Shichi-Go-San number
def is_shichigosan(num):
    count_7, count_5, count_3 = count(num)
    if count_7 >= 1 and count_5 >= 1 and count_3 >= 1:
        return True
    else:
        return False

# Count the Shichi-Go-San numbers between 1 and n
count_shichigosan = 0
for i in range(1, n+1):
    if is_shichigosan(i):
        count_shichigosan += 1
print(count_shichigosan)

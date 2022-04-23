

n = int(input())

# count the number of zeros
counter_zeros = 0
for i in range(n):
    s = input()
    for c in s:
        if c == '0':
            counter_zeros += 1

# count the number of ones
counter_ones = 0
for i in range(n):
    s = input()
    for c in s:
        if c == '1':
            counter_ones += 1

# the answer is the minimum of the number of zeros and the number of ones
print(min(counter_zeros, counter_ones))

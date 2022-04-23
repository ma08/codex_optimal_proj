

s = input().strip()

# count the number of consecutive black tiles
counter = 0
for c in s:
    if c == '0':
        counter += 1

# count the number of consecutive black tiles but ignoring the beginning and ending of the string
# this is done by counting the number of consecutive '0' characters starting from the beginning of the string
# and the number of consecutive '0' characters starting from the end of the string
# we take the maximum of the two
counter_ignore_ends = 0
counter_end = 0
for c in s:
    if c == '0':
        counter_ignore_ends += 1
    else:
        break
for c in reversed(s):
    if c == '0':
        counter_end += 1
    else:
        break
counter_ignore_ends = max(counter_ignore_ends, counter_end)  # this is the number we want

# the answer is the minimum of the two
print(min(counter, counter_ignore_ends))  # this is the answer

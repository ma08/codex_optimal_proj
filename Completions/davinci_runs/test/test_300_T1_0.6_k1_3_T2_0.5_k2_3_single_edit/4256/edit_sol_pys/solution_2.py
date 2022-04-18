

# initial input of 2 numbers
a, b = map(int, input().split())

# count up
count = 0
while b >= a:
    b -= a
    count += 1

# output
print(count)



# initial input
a, b, c = map(int, input().split())

# count up
count = 0
while b >= a and count < c:
    b -= a
    count += 1

# output
print(count)
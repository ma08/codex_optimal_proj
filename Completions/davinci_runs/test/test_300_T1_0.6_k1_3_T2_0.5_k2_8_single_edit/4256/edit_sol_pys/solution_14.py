

# initial input
a = int(input())
b = int(input())
c = int(input())

# count up
count = 0
while b >= a and count < c:
    b -= a
    count += 1

# output
print(count)

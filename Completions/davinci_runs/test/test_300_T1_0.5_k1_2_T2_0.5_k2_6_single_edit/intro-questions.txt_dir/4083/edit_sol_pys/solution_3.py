

# read the input
# n = number of houses
# k = number of colors
# a = list of colors

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

# find the first and last color
first = min(a)
last = max(a)

# find the number of colors between them
# we add 1 to k because the first and last colors are included
# we substract 1 to the result because we can't paint the first and last colors
# the same color
print(k - (last - first + 1))

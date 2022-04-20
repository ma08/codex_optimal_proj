

n, k = map(int, input().split())
a = list(map(int, input().split()))

# find the maximum value in the array
max_val = max(a)

# find the number of times we need to divide by 2 to get to k
num_divs = 0
while max_val > k:
    max_val //= 2
    num_divs += 1

print(num_divs)

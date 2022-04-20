
n, k = map(int, input().split())
a = list(map(int, input().split()))
# find the minimum value in the array
min_val = min(a)

# find the number of times we need to divide by 2 to get to k
num_divs = 0
while min_val > k:
    min_val //= 2
    num_divs += 1

print(num_divs)


n, k = map(int, input().split())
a = list(map(int, input().split()))

# find the minimum value in the array and the number of times we need to divide by 2 to get to k
min_val = min(a)
num_divs = 0
while min_val > k:
    min_val //= 2
    num_divs += 1

print(num_divs)

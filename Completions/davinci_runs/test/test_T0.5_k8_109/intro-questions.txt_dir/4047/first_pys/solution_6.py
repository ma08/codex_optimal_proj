

n = int(input())
x = list(map(int, input().split()))

min_x = min(x)
max_x = max(x)

# The answer is the number of chips with the minimum coordinate + the number of chips with the maximum coordinate.
print(x.count(min_x) + x.count(max_x))
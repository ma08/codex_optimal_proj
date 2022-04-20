

#-----Solution-----

n = int(input())
a = input()
f = list(map(int, input().split()))

# First determine the best segment to modify

# Starting from the left, find the first digit that can be increased
left = 0
while left < n and f[int(a[left]) - 1] <= int(a[left]):
    left += 1

# Starting from the right, find the first digit that can be increased
right = n - 1
while right >= 0 and f[int(a[right]) - 1] <= int(a[right]):
    right -= 1

# If no digits can be increased, the answer is just a
if left == n or right == -1:
    print(a)

# If a digit can be increased, increase the first digit that can be increased
else:
    print(a[:left] + str(f[int(a[left]) - 1]) + a[left + 1:])
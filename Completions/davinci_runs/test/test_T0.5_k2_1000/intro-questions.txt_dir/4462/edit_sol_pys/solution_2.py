

# Input
N = int(input())
a = list(map(int, input().split()))

# Initialization
odd_count = 0

# Count the number of odd numbers
for i in range(N):
    if a[i] % 2 == 1:
        odd_count += 1

# If the number of odd numbers is even, Snuke can achieve his goal
if odd_count % 2 == 0:
    print("Yes")
else:
    print("No")

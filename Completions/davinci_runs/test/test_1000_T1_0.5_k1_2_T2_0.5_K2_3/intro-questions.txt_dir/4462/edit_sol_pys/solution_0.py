
# input
N = int(input())
a = list(map(int, input().split()))

# initialization
odd_count = 0

# count the number of odd numbers in the array
for i in range(N):
    if a[i] % 2 == 1:
        odd_count += 1

# if the number of odd numbers is even, Snuke can achieve his objective
if odd_count % 2 == 0:
    print("Yes")
else:
    print("No")

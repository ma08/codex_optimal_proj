

# read the first line
N = int(input())

# read the second line
A = list(map(int, input().split()))

# check if all even numbers are divisible by 3 or 5
for i in range(N):
    if A[i] % 2 == 0 and A[i] % 3 != 0 and A[i] % 5 != 0:
        print("DENIED")
        exit()

# if all even numbers are divisible by 3 or 5
print("APPROVED")
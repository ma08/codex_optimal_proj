
import sys

# Read from standard input
N, M = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))

# Sort the list of assignments in decreasing order
A.sort(reverse=True)

# Count the number of days that Takahashi can hang out
hang_out_days = 0
for i in range(M):
    # If the number of days he can hang out is less than the number of days he needs to finish the assignment,
    # he cannot finish all the assignments during the vacation
    if hang_out_days < A[i]:
        print(-1)
        sys.exit()
    hang_out_days += 1
    hang_out_days -= A[i]

# Print the result
print(N - M)
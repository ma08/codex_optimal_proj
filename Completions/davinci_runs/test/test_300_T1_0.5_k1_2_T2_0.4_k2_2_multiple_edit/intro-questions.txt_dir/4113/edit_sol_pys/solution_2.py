# read input
import sys
# iterate through all possible values of i
n = int(sys.stdin.readline().rstrip())

# check if the remainders are equal to zero
for i in range(n // 4 + 1):
    if (n - 4 * i) % 7 == 0:
        print("Yes")
        sys.exit()

print("No")

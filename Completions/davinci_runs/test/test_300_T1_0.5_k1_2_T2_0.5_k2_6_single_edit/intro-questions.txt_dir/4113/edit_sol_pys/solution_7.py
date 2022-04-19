
import sys

n = int(sys.stdin.readline().rstrip())

if n % 4 == 0 or n % 7 == 0 or n % 11 == 0:
    print("Yes")
else:
    for i in range(n // 4 + 1):
        if (n - 4 * i) % 7 == 0:
            print("Yes")
            sys.exit()

print("No")

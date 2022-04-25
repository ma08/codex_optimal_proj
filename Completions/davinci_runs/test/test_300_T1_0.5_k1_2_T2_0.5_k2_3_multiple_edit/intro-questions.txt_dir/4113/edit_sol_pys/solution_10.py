import sys

n = int(sys.stdin.readline().strip())

for i in range(n // 4 + 1):
    if (n - 4 * i) % 7 == 0:
        print("Yes")
        sys.exit()

print("No")

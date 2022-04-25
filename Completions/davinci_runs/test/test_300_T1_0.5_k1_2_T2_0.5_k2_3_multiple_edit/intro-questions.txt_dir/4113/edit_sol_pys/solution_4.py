import sys

n = int(sys.stdin.readline().strip())

for i in range(n // 7 + 1):
    if (n - 7 * i) % 4 == 0:
        print("Yes")
        sys.exit()

print("No")

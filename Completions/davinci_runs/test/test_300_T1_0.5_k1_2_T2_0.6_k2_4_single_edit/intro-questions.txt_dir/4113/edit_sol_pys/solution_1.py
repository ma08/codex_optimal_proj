import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N // 4 + 1):
    if (N - 4 * i) % 7 == 0:
        print("Yes")
        sys.exit()

print("No")

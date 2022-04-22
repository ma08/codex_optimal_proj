
import sys
x = int(input())
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    a, b = [int(m) for m in sys.stdin.readline().rstrip().split()]
    print(a + b)
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n // 4 + 1):
    if (n - 4 * i) % 7 == 0:
        print("Yes")
        sys.exit()

print("No")

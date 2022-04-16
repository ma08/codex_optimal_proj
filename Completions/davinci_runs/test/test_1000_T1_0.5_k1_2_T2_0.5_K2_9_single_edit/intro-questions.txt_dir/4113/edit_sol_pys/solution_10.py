
import sys

n = int(sys.stdin.readline())

print("Yes") if n % 7 == 0 or '7' in str(n) else print("No")

import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))

mean = sum(x) / n
diff = [abs(mean - x[i]) for i in range(n)]

print(sum(diff))

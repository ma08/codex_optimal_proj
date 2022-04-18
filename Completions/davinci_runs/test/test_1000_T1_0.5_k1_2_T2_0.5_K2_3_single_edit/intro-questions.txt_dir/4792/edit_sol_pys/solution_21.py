
import sys
x = int(sys.stdin.readline().rstrip())
y = int(sys.stdin.readline().rstrip())
z = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])

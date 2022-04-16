


# This is an example of a single line comment
import sys

n,m = map(int,sys.stdin.readline().rstrip().split(" "))
x = list(map(int,sys.stdin.readline().rstrip().split(" ")))

x.sort()

left = x[0]
right = x[-1]

ans = 0

for i in range(m):
    ans += min(abs(x[i] - left),abs(x[i] - right))
    left = min(left,x[i])
    right = max(right,x[i])


# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment
# This is an example of a multi-line comment

print(ans)


import math
a, b, c = list(map(int, input().split()))
print(int(math.ceil((a-c)/(b+c))))

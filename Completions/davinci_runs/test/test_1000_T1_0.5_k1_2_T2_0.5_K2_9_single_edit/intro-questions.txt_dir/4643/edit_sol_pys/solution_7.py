
import math
n, k = map(int, input().split())
p = list(map(int, input().split()))
print(math.ceil(sum(p)/k))

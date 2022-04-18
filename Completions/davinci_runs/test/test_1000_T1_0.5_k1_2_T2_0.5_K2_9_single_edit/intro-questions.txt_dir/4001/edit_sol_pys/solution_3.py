
import math
N, X = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
print(int(math.ceil((X - sum(x)) / min(x))))

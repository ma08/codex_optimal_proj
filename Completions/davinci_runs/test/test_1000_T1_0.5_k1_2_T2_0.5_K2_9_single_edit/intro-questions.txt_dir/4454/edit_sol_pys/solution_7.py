import math

q = int(input())

for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(math.ceil(sum(a) / n))

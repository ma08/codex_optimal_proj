
# My Solution
import random

n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    a.sort()
    attack = random.randint(0, len(a)-1)
    defend = random.randint(0, len(a)-1)
    if a[attack] > a[defend]:
        a[defend] = 0
        a = [i for i in a if i != 0]
    else:
        a[attack] = 0
        a = [i for i in a if i != 0]
print(a[0])

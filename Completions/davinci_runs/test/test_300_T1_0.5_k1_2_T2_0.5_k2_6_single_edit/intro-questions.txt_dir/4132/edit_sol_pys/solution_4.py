

# My Solution
import random

n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    a.sort()
    attacker = random.randint(0, len(a) - 1)
    victim = random.randint(0, len(a) - 1)
    if a[attacker] > a[victim]:
        a.pop(victim)
    else:
        a.pop(attacker)
print(a[0])

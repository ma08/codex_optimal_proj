
# My Solution
import random

n = int(input())
a = list(map(int, input().split()))

while len(a) > 1:
    a.sort()
    attacker = a[random.randint(0, len(a) - 1)]
    victim = a[random.randint(0, len(a) - 1)]
    if attacker > victim:
        a.remove(victim)
        a = [i for i in a if i != 0]
    else:
        a.remove(attacker)
        a = [i for i in a if i != 0]
print(a[0])



# My Solution
import random

n = int(input())
a = list(map(int, input().split()))
def find_random_attacker(n):
    return random.randint(0, n-1)

def find_random_victim(n):
    return random.randint(0, n-1)

def find_random_attacker_and_victim(n):
    return find_random_attacker(n), find_random_victim(n)


while len(a) > 1:
    a.sort()
    attacker, victim = find_random_attacker_and_victim(len(a))
    if a[attacker] > a[victim]:
        a[victim] = 0
        a = [i for i in a if i != 0]
    else:
        a[attacker] = 0
        a = [i for i in a if i != 0]
print(a[0])

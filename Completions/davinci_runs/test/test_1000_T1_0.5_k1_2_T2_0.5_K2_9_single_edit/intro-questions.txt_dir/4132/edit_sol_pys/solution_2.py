

# My Solution
# import random

# n = int(input())
# a = list(map(int, input().split()))

# while len(a) > 1:
#     a.sort()
#     attacker = random.randint(0, len(a)-1)
#     victim = random.randint(0, len(a)-1)
#     if a[attacker] > a[victim]:
#         a[victim] = 0
#         a = [i for i in a if i != 0]
#     else:
#         a[attacker] = 0
#         a = [i for i in a if i != 0]
# print(a[0])

# Solution

from random import randint

n = int(input())  # number of warriors
a = list(map(int, input().split()))  # list of warriors' power

while len(a) > 1:  # while there are more than one warrior
    a.sort()  # sort the list
    attacker = randint(0, len(a)-1)  # choose a warrior to attack
    victim = randint(0, len(a)-1)  # choose a warrior to be attacked
    if a[attacker] > a[victim]:  # if attacker's power is greater than victim's
        a[victim] = 0  # then kill the victim
        a = [i for i in a if i != 0]  # remove the killed warrior
    else:  # if attacker's power is less than victim's
        a[attacker] = 0  # then kill the attacker
        a = [i for i in a if i != 0]  # remove the killed warrior

print(a[0])  # print the last warrior's power

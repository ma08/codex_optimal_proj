
# My Solution
import random

n = int(input())
a = list(map(int, input().split()))  # create a list of integers

while len(a) > 1:  # while there are more than one elements in the list
    a.sort()  # sort the list
    attacker = random.randint(0, len(a)-1)  # choose a random index
    victim = random.randint(0, len(a)-1)  # choose a random index
    if a[attacker] > a[victim]:  # if the attacker's value is greater than the victim's
        a[victim] = 0  # set the victim's value to 0
        a = [i for i in a if i != 0]  # remove all 0s from the list
    else:
        a[attacker] = 0
        a = [i for i in a if i != 0]
print(a[0])


import sys

n = int(input())

q = sys.stdin.readline()

x = int(input()) 

num_men = 0
num_women = 0
max_people = 0

for person in q:
    if person == 'M':
        num_men += 1
    else:
        num_women += 1

    if abs(num_men - num_women) > x:
        break
    else:
        max_people += 1

print(max_people)

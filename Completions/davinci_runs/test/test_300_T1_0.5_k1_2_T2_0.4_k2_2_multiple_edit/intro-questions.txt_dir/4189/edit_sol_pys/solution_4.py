

from collections import Counter 
n = int(input())
c = Counter([input().split()[1] for _ in range(n)])
print(c['soft']*c['hard'])

n = int(input())
soft, hard = 0, 0
for _ in range(n):
    name, type = input().split()
    if type == 'soft':
        soft += 1
    elif type == 'hard':
        hard += 1
print(soft*hard)

n = int(input())
soft, hard = 0, 0
for _ in range(n):
    name, type = input().split()
    if type == 'soft':
        soft += 1
    elif type == 'hard':
        hard += 1
print(soft*hard)



# from collections import Counter
# n = int(input())
# c = Counter([input().split()[1] for _ in range(n)])
# print(c['soft']*c['hard'])

n = int(input())
soft = 0
hard = 0
for _ in range(n):
    name, typ = input().split()
    if typ == 'soft':
        soft += 1
    elif typ == 'hard':
        hard += 1
print(soft*hard)

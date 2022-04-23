

# from collections import Counter
# n = int(input())
# c = Counter([input().split()[1] for _ in range(n)])
# print(c['soft']*c['hard'])

n = int(input())
soft = hard = 0
for _ in range(n):
    name, text = input().split()
    if text == 'soft':
        soft += 1
    elif text == 'hard':
        hard += 1
print(soft*hard)



# from collections import Counter
# n = int(input())
# c = Counter([input().split()[1] for _ in range(n)])
# print(c['soft']*c['hard'])

n = int(input())
l = []
for i in range(n):
    l.append(input().split()[1])
c = Counter(l)
print(c['soft'] * c['hard'])

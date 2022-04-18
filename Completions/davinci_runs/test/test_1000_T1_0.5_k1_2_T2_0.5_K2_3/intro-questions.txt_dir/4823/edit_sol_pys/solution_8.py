

from collections import defaultdict

n = int(input())

d = defaultdict(list)

for i in range(n):
    word = input()
    d[word].append(i+1)

q = int(input())

for i in range(q):
    word = input()
    if word in d:
        print(' '.join(map(str, d[word])))
    else:
        print('-1')

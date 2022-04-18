import collections

n = int(input('Enter n: '))
s = [input('Enter element: ') for _ in range(n)]

c = collections.Counter(s).most_common()
print(c)

for i in c:
    if i[1] == c[0][1]:
        print(i[0])

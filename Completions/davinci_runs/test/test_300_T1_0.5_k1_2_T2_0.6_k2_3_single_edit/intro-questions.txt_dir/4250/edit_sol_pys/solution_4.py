
#!/bin/python3
nk = input().split()
n = int(nk[0])
k = int(nk[1])
a = list(map(int, input().rstrip().split()))
count = []
unique = []
for i in set(a):
    count.append(a.count(i))
    unique.append(i)
zipped_pairs = zip(count, unique)
z = [x for _, x in sorted(zipped_pairs)]
for i in range(k):
    print(z[i])

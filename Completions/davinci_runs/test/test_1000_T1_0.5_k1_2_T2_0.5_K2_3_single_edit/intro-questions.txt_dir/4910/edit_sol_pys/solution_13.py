

import sys
#import math

#s = sys.stdin.readline()
#s = s.rstrip()
#s = s.split()

#s = "10 ghost mummy witch demon demon demon demon demon demon demon"
#s = s.split()

#n = int(s[0])
#s = s[1:]

#d = {}

#for i in range(n):
#    if s[i] not in d:
#        d[s[i]] = 1
#    else:
#        d[s[i]] += 1

#m = max(d.values())

#for k, v in d.items():
#    if v == m:
#        print(k)



#s = "1 2 3 4 5 6 7 8 9 10"
#s = s.split()

#n = len(s)

#for i in range(n):
#    for j in range(i + 1, n):
#        if int(s[i]) > int(s[j]):
#            s[i], s[j] = s[j], s[i]

#print(s)







s = "1 2 3 4 5 6 7 8 9 10"
s = s.split()

n = len(s)

for i in range(n):
    for j in range(i + 1, n):
        if int(s[i]) > int(s[j]):
            s[i], s[j] = s[j], s[i]

print(s)

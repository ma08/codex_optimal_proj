

import sys

s = sys.stdin.readline()

# Counting the number of letters
count = [0]*26
for c in s:
    count[ord(c)-ord('a')] += 1

# Counting the number of odd letters
odd = 0
for c in count:
    if c % 2 == 1:
        odd += 1

if odd > 1:
    print odd - 1
else:
    print 0

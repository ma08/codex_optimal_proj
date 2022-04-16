

import sys
import re

n = int(input())

words = input().split()

if re.match(r'^[0-9]+$', words[0]):
    if int(words[0]) != 1:
        print("something is fishy")
        sys.exit(0)
else:
    print("something is fishy")
    sys.exit(0)

for i in range(1, n):
    if re.match(r'^[0-9]+$', words[i]):
        if int(words[i]) != int(words[i-1]) + 1:
            print("something is fishy")
            sys.exit(0)
    else:
        continue

print("makes sense")

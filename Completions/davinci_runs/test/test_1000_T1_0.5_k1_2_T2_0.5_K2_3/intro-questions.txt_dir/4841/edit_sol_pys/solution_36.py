

import sys
import re

n = int(sys.stdin.readline())

words = sys.stdin.readline().split()

if re.match(r'^[0-9]+$', words[0]):
    if int(words[0]) != 1:
        print("Something is fishy")
        sys.exit(0)
else:
    print("Something is fishy")
    sys.exit(0)
    
for i in range(1, n):
    if re.match(r'^[0-9]+$', words[i]):
        if int(words[i]) != int(words[i-1]) + 1:
            print("Something is fishy")
            sys.exit(0)
    else:
        continue

print("makes sense")

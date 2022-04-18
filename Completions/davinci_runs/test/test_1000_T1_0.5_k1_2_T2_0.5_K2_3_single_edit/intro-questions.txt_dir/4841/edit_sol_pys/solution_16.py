

import sys
import re
n = int(sys.stdin.readline())
words = sys.stdin.readline().split()

if re.match(r'^[0-9]+$', words[0]):  # if first word is a number
    if int(words[0]) != 1:  # if first number is not 1
        print("something is fishy")
        sys.exit(0)
else:  # if first word is not a number
    print("something is fishy")
    sys.exit(0)

for i in range(1, n):
    if re.match(r'^[0-9]+$', words[i]):  # if word is a number
        if int(words[i]) != int(words[i-1]) + 1:  # if number is not a consecutive number
            print("something is fishy")
            sys.exit(0)
    else:  # if word is not a number
        continue

print("makes sense")

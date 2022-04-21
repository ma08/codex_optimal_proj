import os

import sys

s = input()
s = s.rstrip('\r\n')
print(s)

print(os.path.splitext(s)[0])

print("No")

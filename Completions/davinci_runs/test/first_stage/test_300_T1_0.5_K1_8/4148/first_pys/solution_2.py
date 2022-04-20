

import string

n = int(input())
s = input()

alphabet = string.ascii_uppercase

for c in s:
    print(alphabet[(alphabet.index(c) + n) % len(alphabet)], end="")
print()
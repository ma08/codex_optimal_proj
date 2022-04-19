import os

import tempfile
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip().split()

f = tempfile.TemporaryFile('w+t')

for i in range(n):
    f.write(s[i])
    f.seek(0)
    if i > 1 and f.read()[-1] == f.read()[-2]:
        os.remove(f.name)

print(n - len(stack))
print(''.join(stack))

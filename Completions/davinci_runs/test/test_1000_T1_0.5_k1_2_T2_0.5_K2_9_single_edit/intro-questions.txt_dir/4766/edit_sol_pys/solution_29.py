

import sys

num_lines = int(sys.stdin.readline())

for line in sys.stdin.readlines():
    if line[:11] == 'Simon says':
        print(line[11:])

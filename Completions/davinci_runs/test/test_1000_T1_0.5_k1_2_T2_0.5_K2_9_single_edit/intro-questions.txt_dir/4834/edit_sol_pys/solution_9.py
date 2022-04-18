

import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

teams.sort()

print(sum(teams[0::2]) + sum(teams[1::2]))

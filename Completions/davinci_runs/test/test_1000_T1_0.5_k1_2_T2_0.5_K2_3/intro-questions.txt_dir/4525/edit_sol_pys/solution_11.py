

# SOLUTION

#!/usr/bin/env python3

from sys import stdin, stdout

def main():
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        if n == 2:
            stdout.write('YES\n')
            stdout.write('1 2\n')
        elif n == 4:
            stdout.write('YES\n')
            stdout.write('2 4 1 3\n')
        else:
            stdout.write('YES\n')
            stdout.write(' '.join(map(str, list(range(2, n, 2)) + list(range(1, n, 2)))) + '\n')

main()

import sys

n = int(sys.stdin.readline().strip())
print('Alice' if n % 2 == 1 else 'Bob')

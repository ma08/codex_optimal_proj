

import sys

def is_lucky(n):
    n = str(n)
    half = len(n) // 2
    return sum([int(n[i]) for i in range(half)]) == sum([int(n[i]) for i in range(half, len(n))])

if __name__ == '__main__':
    n = sys.stdin.readline()
    print('Yes' if is_lucky(n) else 'No')
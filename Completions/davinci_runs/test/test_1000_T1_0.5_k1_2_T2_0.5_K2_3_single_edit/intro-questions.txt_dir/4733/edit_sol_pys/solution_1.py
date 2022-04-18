

import sys

def main():
    x = int(sys.stdin.readline())
    shuffle = sys.stdin.readline().strip()
    if shuffle == 'out':
        if x % 2 == 0:
            print(x // 2)
        else:
            print((x + 1) // 2)
    elif shuffle == 'in':
        if x % 2 == 0:
            print(x - 1)
        else:
            print(x)
main()

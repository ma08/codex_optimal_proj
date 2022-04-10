

import sys

def main():
    n = int(sys.stdin.readline().strip())

    if n % 2 == 0:
        result = n/2
    else:
        result = n - 1

    print(int(result))

main()
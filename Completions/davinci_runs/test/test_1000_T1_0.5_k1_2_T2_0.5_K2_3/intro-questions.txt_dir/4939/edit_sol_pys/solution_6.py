

import sys

def main():
    n, m = [int(x) for x in sys.stdin.readline().split()]
    data = [int(x) for x in sys.stdin.readline().split()]
    data.sort()
    print(data)

main()

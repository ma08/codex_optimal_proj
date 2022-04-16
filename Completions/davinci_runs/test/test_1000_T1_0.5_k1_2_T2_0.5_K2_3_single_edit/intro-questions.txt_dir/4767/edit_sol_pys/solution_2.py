

import sys

def main():
    vals = [int(x) for x in sys.stdin.readline().split()]
    print(19 - min(vals))

main()

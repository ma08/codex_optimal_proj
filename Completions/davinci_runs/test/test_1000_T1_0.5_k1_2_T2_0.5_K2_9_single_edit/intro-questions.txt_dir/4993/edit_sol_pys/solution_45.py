

import sys

def main():
    P, N = [int(i) for i in sys.stdin.readline().split()]
    parts = []
    for line in sys.stdin:
        line = line.strip()
        parts.append(line)
        if len(parts) == P:
            print(len(parts))
            return
        if len(parts) > P:
            print("paradox avoided")
            return
    else:
        print("paradox avoided")

main()

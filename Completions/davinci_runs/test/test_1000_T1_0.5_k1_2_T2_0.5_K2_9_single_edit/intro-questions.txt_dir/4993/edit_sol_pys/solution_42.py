

import sys

    # read the number of parts and number of days
def main():
    # set of parts
    P, N = map(int, sys.stdin.readline().split())
    parts = set()
    for i in range(N):
        part = sys.stdin.readline().strip()
        if part not in parts:
            parts.add(part)
        if len(parts) == P:
            print(i + 1)
            return

    print("paradox avoided")

if __name__ == '__main__':
    main()

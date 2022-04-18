

import sys

def main():
    while True:
        P, N = map(int, sys.stdin.readline().split())
        if P == 0 and N == 0:
            break
        parts = set()
        for i in range(N):
            part = sys.stdin.readline().strip()
            if part not in parts:
                parts.add(part)
            if len(parts) == P:
                print(i + 1)
                break
        else:
            print("paradox avoided")


if __name__ == '__main__':
    main()

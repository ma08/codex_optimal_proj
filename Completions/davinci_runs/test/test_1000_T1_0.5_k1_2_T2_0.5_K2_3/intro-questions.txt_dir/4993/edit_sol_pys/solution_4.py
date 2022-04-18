
import sys


def main():
    P, N = map(int, sys.stdin.readline().split())  # P: number of parts, N: number of days
    parts = set()
    for i in range(N):
        part = sys.stdin.readline().strip()
        if part not in parts:  # if the part is not in the set, add the part
            parts.add(part)
        if len(parts) == P:
            print(i + 1)
            return

    print("paradox avoided")


if __name__ == '__main__':
    main()

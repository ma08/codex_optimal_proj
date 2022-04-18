
import sys

def main():
    P, N = map(int, input().split())
    parts = set()
    for i in range(N):
        part = input()
        if part not in parts:
            parts.add(part)
        if len(parts) == P:
            print(i + 1)
            return

    print("paradox avoided")

if __name__ == '__main__':
    main()

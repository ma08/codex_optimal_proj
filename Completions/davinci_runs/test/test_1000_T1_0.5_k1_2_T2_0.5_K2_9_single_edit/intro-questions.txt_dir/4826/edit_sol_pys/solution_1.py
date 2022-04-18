
import sys

def who_wins(n):
    return "Alice" if n % 2 == 1 else "Bob"

def main():
    n = int(sys.stdin.readline().strip())
    print(who_wins(n))

if __name__ == '__main__':
    main()

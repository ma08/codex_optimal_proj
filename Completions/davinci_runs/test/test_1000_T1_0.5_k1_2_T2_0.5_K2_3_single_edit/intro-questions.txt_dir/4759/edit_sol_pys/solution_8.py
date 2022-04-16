
import sys

def find_all_occurrences(s, c):
    return [i for i, letter in enumerate(s) if letter == c]

def main():
    s = sys.stdin.readline().strip()
    c = sys.stdin.readline().strip()
    print(*find_all_occurrences(s, c))

if __name__ == '__main__':
    main()

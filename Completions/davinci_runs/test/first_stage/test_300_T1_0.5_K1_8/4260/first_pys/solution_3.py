

import sys

def main():
    args = sys.argv
    if len(args) != 1:
        print("usage: python3 {0} < input.txt > output.txt".format(args[0]))
        sys.exit(1)
    for line in sys.stdin:
        t, x = map(int, line.split())
        print(t / x)

if __name__ == '__main__':
    main()
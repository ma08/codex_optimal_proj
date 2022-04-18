

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) <= 2:
            print(0)
        elif len(set(line)) <= 2:
            print(0)
        else:
            print(len(line) - 2)

if __name__ == '__main__':
    main()
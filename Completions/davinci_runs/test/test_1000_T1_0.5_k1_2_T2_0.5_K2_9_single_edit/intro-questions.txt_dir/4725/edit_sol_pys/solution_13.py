
import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if len(line) <= 2:
            print(0, end='')
        elif len(set(line)) <= 2:
            print(0, end='')
        else:
            print(len(line) - 2, end='')

if __name__ == '__main__':
    main()

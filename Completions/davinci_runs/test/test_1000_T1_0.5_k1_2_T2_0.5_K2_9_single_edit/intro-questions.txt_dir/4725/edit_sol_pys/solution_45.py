
import sys

def main():
    for line in sys.stdin:
        line = line.strip().split(' ')
        print(line)

if __name__ == '__main__':
    main()

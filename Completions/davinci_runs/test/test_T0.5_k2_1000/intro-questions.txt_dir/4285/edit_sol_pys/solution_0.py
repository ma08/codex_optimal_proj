
import sys

def main():
    # read number of lines
    n = int(sys.stdin.readline().strip())

    # read lines
    lines = [sys.stdin.readline().strip() for _ in range(n)]

    # count number of lines containing "cat"
    count = 0
    for line in lines:
        if 'cat' in line:
            count += 1

    print(count)

if __name__ == '__main__':
    main()

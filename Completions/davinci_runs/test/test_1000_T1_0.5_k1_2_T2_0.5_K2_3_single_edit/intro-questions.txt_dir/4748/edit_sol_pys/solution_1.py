

import sys

def main():
    lines = sys.stdin.readlines()
    n, m = [int(x) for x in lines[0].split()]
    count = 0
    for i in range(n):
        count += len(lines[i+1].strip())
    print(count)


if __name__ == '__main__':
    main()

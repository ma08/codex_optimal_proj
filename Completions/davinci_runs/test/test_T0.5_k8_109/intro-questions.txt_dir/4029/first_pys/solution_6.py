

import sys

def main():
    line = sys.stdin.readline()
    n = int(line)
    if n % 25 == 0:
        print(0)
        return
    for i in range(len(line) - 1):
        if int(line[i] + line[i + 1]) % 25 == 0:
            print(1)
            return
    print(-1)

if __name__ == '__main__':
    main()


import sys

def count_shichigo_san(n):
    n = str(n)
    count = 0
    for i in range(len(n)):
        if n[i] == '3' or n[i] == '5' or n[i] == '7':
            count += 1
    return count

def main():
    n = int(sys.stdin.readline().rstrip())
    count = 0
    for i in range(1, n + 1):
        if count_shichigo_san(i) >= 3:
            count += 1
    print(count)

if __name__ == '__main__':
    main()
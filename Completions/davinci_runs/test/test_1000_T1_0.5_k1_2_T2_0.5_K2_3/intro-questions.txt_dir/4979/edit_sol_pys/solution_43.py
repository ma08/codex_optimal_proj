import sys

def main():
    num = int(sys.stdin.readline().strip())
    rev = 0

    while num > 0:
        rev = rev << 1
        rev = rev | (num & 1)
        num = num >> 1

    print(rev)

if __name__ == '__main__':
    main()

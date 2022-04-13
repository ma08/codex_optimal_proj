import sys

def main():
    num = int(sys.stdin.readline())
    rev_num = 0

    while num > 0:
        rev_num = rev_num << 1 | (num & 1)
        num = num >> 1

    print(rev_num)

if __name__ == '__main__':
    main()

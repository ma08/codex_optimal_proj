import sys

def main():
    num = int(sys.stdin.readline())
    rev_num = 0

    while num > 0:
        rev_num = rev_num * 2
        rev_num = rev_num + (num % 2)
        num = num // 2

    print(rev_num)

if __name__ == '__main__':
    main()

import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n // 100000 == 555 and n // 10000 % 10 == 5 and n // 1000 % 10 == 5:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()

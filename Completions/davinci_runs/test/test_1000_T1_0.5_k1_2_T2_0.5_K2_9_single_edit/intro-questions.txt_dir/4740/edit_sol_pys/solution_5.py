import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n // 100000 == 555:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()

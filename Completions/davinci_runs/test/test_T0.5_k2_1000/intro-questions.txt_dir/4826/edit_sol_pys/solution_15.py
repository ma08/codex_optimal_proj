import sys

def main():
    n = int(sys.stdin.readline().strip())
    if n % 2 == 1:
        print('Alice')
    else:
        print('Bob')

if __name__ == '__main__':
    main()

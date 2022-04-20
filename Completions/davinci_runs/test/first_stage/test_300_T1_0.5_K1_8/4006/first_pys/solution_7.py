
import sys

def main():
    n = int(sys.stdin.readline())
    if n == 1:
        print(2)
        return
    if n % 10 == 0:
        print(19)
        return
    print(20)

if __name__ == '__main__':
    main()
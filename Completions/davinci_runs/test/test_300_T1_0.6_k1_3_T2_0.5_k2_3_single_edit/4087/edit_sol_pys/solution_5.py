import sys

def sumDigits(n):
    return sum(map(int, list(str(n)))) % 4 == 0

def main():
    a = int(sys.stdin.readline())
    if sumDigits(a):
        print(a)
    else:
        print(a + (4 - (sumDigits(a) % 4)))

if __name__ == '__main__':
    main()

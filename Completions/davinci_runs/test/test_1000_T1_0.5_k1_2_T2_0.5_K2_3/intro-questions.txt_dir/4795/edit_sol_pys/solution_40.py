import sys

def main():
    pass

def solve(num):
    num = str(num)
    length = len(num)
    if length == 1:
        return int(num)
    else:
        return int(num[0])**(length-1) + int(num[1:])

def read_int():
    return int(sys.stdin.readline().strip())

if __name__ == '__main__':
    main()

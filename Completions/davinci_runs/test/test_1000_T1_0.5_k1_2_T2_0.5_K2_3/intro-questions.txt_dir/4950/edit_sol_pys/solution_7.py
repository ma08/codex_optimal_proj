
import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    print(a[-1] - a[0]) 


if __name__ == '__main__':
    main()

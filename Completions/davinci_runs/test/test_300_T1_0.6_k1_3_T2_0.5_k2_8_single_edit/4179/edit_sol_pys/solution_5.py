
import sys

def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    print(sum(a[i] * b[i] for i in range(n)))

if __name__ == '__main__':
    main()

import sys

def main():
    num = int(input())
    for i in range(num):
        a, b = map(int, input().split())
        print(a+b)

if __name__ == '__main__':
    main()

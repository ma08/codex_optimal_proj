import sys

def main():
    N = int(input())
    a = [int(input()) for _ in range(N)]
    a.sort(reverse=True)
    print(a)

if __name__ == '__main__':
    main()

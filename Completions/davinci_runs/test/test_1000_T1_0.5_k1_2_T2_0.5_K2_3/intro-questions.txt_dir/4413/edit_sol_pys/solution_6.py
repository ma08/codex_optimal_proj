# coding: utf-8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(len(set(a)))


if __name__ == '__main__':
    main()

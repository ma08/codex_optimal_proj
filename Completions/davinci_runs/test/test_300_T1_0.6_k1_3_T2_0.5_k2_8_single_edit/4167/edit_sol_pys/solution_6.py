import sys


def main():
    N, K = map(int, input().split())
    print(K * (K - 1)**(N - 1))

if __name__ == '__main__':
    main()

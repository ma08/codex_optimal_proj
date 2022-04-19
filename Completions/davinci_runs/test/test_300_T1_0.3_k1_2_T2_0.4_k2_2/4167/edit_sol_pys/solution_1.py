
import math

def main():
    N, K = map(int, input().split())
    print(math.ceil(N / K) * math.ceil(N / K) * math.ceil(N / K))


if __name__ == '__main__':
    main()

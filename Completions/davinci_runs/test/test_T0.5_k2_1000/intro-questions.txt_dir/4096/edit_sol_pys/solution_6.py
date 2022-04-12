import math

def main():
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()))

    print(math.ceil(m / a[-1]))


if __name__ == "__main__":
    main()

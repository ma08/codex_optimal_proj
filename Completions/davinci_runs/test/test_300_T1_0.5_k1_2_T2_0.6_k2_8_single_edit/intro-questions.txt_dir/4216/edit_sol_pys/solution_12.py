import math

def main():
    x = int(input())
    n = int(input())

    ans = 0
    for i in range(n):
        ans += x * 10 ** i
    print(ans)


if __name__ == '__main__':
    main()

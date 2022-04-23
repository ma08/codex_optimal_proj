import math



def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = math.ceil(n / 2)
    print(ans)


if __name__ == '__main__':
    main()

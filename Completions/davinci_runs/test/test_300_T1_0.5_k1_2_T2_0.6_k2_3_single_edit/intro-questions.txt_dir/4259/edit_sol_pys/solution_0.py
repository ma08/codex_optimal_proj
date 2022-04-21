
import math


def main():
    k = int(input())
    a, b = map(int, input().split())
    ans = "OK" if math.ceil(b / k) >= math.floor(a / k) else "NG"
    print(ans)

if __name__ == '__main__':
    main()

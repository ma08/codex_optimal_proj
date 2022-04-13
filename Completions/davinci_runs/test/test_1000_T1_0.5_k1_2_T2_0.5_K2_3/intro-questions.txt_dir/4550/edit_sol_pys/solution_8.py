import math


def main():
    a, b, c = map(int, input().split())
    if a + b > c and a + c > b and b + c > a:
        print("YES")
    else:
        print("No")

if __name__ == "__main__":
    main()

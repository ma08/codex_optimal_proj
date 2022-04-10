
import sys

def main():
    n, d, k = [int(x) for x in input().split()]
    if k == 1:
        print("NO")
        sys.exit()
    if d == 1:
        print("YES")
        for i in range(1, n):
            print(i + 1, i)
        sys.exit()
    print("YES")
    for i in range(1, n):
        print(i + 1, i)
    if d == 2:
        print(3, 1)
    elif d == 3:
        print(2, 1)
        print(3, 2)
    elif d == 4:
        print(2, 1)
        print(3, 2)
        print(4, 1)
    elif d == 5:
        print(2, 1)
        print(3, 2)
        print(4, 1)
        print(5, 1)
    else:
        print("NO")


if __name__ == "__main__":
    main()

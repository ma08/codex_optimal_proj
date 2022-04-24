

from sys import stdin

def main():
    n, d, k = map(int, stdin.readline().strip().split(" "))
    if d == 1:
        print("YES")
        for i in range(1, n):
            print("{} {}".format(i, i + 1))
        return
    if k < d - 1:
        print("NO")
        return
    if n == 2:
        print("YES")
        print("1 2")
        return
    if d == 2:
        print("YES")
        for i in range(1, n):
            print("{} {}".format(i, i + 1))
        return 
    if d == 3:
        print("YES")
        print("{} {}".format(1, n))
        for i in range(1, n - 1):
            print("{} {}".format(i, i + 1))
        return
    if d == 4:
        print("YES")
        print("{} {}".format(1, n))
        print("{} {}".format(1, n - 1))
        print("{} {}".format(2, n - 1))
        for i in range(3, n - 2):
            print("{} {}".format(i, i + 1))
        return
    if d == 5:
        print("YES")
        print("{} {}".format(1, n))
        print("{} {}".format(1, n - 1))
        print("{} {}".format(2, n - 1))
        print("{} {}".format(2, n - 2))
        print("{} {}".format(3, n - 2))
        for i in range(4, n - 3):
            print("{} {}".format(i, i + 1))
        return
    print("NO")

if __name__ == "__main__":
    main()

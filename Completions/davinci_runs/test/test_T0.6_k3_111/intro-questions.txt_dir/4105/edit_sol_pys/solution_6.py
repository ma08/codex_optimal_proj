

import sys

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]

    if (k == 2):
        if (n % 2 == 0):
            print("YES")
            for i in range(0, n, 2):
                print("1 2", end="\n")
        else:
            print("NO")
    elif (n % 2 == 0):
        print("YES")
        for i in range(0, n, 2):
            print(str(i % k + 1) + " " + str(i % k + 2), end="\n")
    else:
        print("NO")

if __name__ == "__main__":
    main()

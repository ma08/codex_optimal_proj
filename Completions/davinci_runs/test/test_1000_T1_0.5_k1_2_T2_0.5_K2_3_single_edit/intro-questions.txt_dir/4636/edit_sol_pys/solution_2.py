
import sys

def main():
    sys.stdin = open("in.txt", "r")
    sys.stdout = open("out.txt", "w")
    t = int(input())
    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        b = [0] * 2
        for j in range(n):
            if j % 2 == 0:
                b[0] += a[j]
            else:
                b[1] += a[j]
        print(b[0], b[1])

if __name__ == "__main__":
    main()

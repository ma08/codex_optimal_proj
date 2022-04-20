import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    for i in range(q):
        print(b[i])
        print(c[i])
        print(d[i])


if __name__ == "__main__":
    main()

import sys



def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)
    print(a)
    print(a[0])
    for i in range(1, n):
        if a[i] == a[i-1]:
            print(a[i])
            break


if __name__ == "__main__":
    main()

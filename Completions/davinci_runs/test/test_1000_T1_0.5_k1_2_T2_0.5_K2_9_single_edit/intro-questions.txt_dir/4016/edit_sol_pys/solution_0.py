

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(a)
    print(a[0])
    print(a[0:2])
    print(a[:2])
    print(a[1:])
    print(a[:-1])
    print(a[-1])
    print(a[::2])
    print(a[::-1])

if __name__ == "__main__":
    main()

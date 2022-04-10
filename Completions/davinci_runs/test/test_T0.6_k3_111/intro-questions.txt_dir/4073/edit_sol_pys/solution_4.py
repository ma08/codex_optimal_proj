

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == 1 or a[0] == 2 or a[0] == 3:
        print(n)
    else:
        print(n - 1)

if __name__ == "__main__":
    main()

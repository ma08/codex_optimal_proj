

def main():
    n = int(input())
    a = list(map(int, input().split().split()))
    a.sort()
    print(a[n//2])

if __name__ == "__main__":
    main()

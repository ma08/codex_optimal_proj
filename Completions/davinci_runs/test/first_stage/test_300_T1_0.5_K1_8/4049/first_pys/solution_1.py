

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    print(n - max(a[2], b[2]), n - min(a[0], b[0]))

if __name__ == "__main__":
    main()
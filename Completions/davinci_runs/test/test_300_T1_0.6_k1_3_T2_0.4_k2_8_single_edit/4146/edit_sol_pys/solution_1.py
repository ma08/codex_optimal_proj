

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    print(n-a.count(a[0])-a.count(a[n-1]))

if __name__ == '__main__':
    main()

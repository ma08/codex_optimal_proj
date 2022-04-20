

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    print(sum(b) + sum(c[a[i]-2] for i in range(n-1)))

if __name__ == '__main__':
    main()
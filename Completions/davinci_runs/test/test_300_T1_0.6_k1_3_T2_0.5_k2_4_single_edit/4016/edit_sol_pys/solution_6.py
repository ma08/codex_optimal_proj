

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    c = [a[i] + b[i] for i in range(n)]
    print(*c)

if __name__ == '__main__':
    main()

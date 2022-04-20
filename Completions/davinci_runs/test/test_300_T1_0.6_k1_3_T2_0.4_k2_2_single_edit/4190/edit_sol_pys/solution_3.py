

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [(a[i] + b[i]) % n for i in range(n)]
    c.sort()
    print(' '.join([str(x) for x in c]))

if __name__ == '__main__':
    main()

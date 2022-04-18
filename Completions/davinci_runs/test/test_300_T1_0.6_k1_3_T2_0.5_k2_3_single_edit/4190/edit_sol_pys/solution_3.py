

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [str((x + y) % n) for (x, y) in zip(a, b)]
    c.sort()
    print(' '.join(c))

if __name__ == '__main__':
    main()

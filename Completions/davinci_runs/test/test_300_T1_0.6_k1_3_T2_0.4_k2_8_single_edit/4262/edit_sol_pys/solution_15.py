

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    print(abs(p.index(1) - q.index(1)) + abs(p.index(2) - q.index(2)) + abs(p.index(3) - q.index(3)))


if __name__ == '__main__':
    main()

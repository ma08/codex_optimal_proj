

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = list(map(int,input().split()))
    print(abs(p.index(1)-q.index(1)) + abs(p.index(2)-q.index(2)) + abs(p.index(3)-q.index(3)) + abs(p.index(4)-q.index(4)) + abs(p.index(5)-q.index(5)) + abs(p.index(6)-q.index(6)) + abs(p.index(7)-q.index(7)) + abs(p.index(8)-q.index(8)) + abs(p.index(9)-q.index(9)))

if __name__ == '__main__':
    main()

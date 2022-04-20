

def main():
    n = int(input())
    a = [int(i) for i in input().split()][:n]
    b = [int(i) for i in input().split()][:n]
    c = [int(i) for i in input().split()][:n]
    a.sort(); b.sort(); c.sort()
    print(a, b, c)

if __name__ == '__main__':
    main()

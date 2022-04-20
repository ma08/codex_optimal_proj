

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    for i in range(1, n):
        print(a[i], end=' ')
    print(a[0])

if __name__ == '__main__':
    main()

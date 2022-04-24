

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = [a[i] - a[i - 1] for i in range(1, n)]
    d.sort()
    if d[0] == d[-1]:
        print(0)
    else:
        print(2)

if __name__ == '__main__':
    main()

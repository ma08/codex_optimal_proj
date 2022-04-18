

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[d[i - 2] + 1] = i
    print(' '.join([str(x) for x in a[1:]]))

if __name__ == '__main__':
    main()

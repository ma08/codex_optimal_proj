
def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    a = [0] * n
    a[0] = 1
    for i in range(1, n):
        a[d[i - 1] + 1] = i + 1
    print(' '.join([str(x) for x in a]))

if __name__ == '__main__':
    main()

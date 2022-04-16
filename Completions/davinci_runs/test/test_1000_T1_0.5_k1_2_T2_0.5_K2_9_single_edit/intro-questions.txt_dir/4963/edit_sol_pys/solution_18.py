
def main():
    line = [int(x) for x in input().split()]
    n = line[0]
    k = line[1]
    d = [int(x) for x in input().split()]
    ans = [0] * n
    ans[0] = 1
    for i in range(n - 1):
        ans[d[i] + 1] = i + 2
    print(' '.join([str(x) for x in ans]))


if __name__ == '__main__':
    main()

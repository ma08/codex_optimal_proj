

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    line = [1] * n
    for i in range(n - 1):
        line[d[i]] = i + 2
    print(' '.join([str(x) for x in line]))

if __name__ == '__main__':
    main()

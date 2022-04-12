

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    l = [0] * n
    l[0] = 0
    for i in range(n - 1):
        l[d[i] + 1] = i + 1
    print(' '.join([str(x) for x in l]))

if __name__ == '__main__':
    main()

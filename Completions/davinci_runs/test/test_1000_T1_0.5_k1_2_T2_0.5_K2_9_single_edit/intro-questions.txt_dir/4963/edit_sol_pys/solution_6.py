

def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    line = [0] * (n + 1)
    line[0] = 1
    for i in range(n):
        line[d[i]] = i + 2
    print(' '.join([str(x) for x in line]))

if __name__ == '__main__':
    main()

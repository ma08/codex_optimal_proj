

def main():
    n = int(input())
    f = list(map(int, input().split()))

    for i in range(n):
        if f[i] == 0:
            for j in range(1, n+1):
                if j not in f and j != i+1:
                    f[i] = j
                    break

    print(' '.join(map(str, f)))

if __name__ == '__main__':
    main()
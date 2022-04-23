

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = i
    print(len(d))
    print(' '.join([str(i) for i in d]))

if __name__ == '__main__':
    main()

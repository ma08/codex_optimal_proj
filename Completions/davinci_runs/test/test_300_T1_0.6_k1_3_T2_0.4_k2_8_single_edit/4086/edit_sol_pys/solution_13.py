

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[a[i]] = i
    print(len(d.keys()))
    print(' '.join(str(i) for i in d.keys()))

if __name__ == '__main__':
    main()



def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        d[i] = a[i]
    d = sorted(d.items(), key=lambda x: x[1])
    for i in range(n):
        print(d[i][0], end=" ")
    print()

if __name__ == '__main__':
    main()

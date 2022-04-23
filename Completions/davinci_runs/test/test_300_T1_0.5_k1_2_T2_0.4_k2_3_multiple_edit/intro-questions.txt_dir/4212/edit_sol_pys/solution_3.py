

def main():
    n = int(input())
    a = list(map(int, input().split()))
    d = [0 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if a[j] < a[i]:
                d[i] = max(d[i], d[j])
        d[i] += 1

    print(max(d))

if __name__ == '__main__':
    main()

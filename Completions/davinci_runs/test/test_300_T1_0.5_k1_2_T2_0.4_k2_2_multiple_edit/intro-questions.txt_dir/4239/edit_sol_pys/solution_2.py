

def main():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    for i in range(n):
        for j in range(i, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)

if __name__ == '__main__':
    main()



def main():
    n = int(input())
    b = list(map(int, input().split()))

    a = [0] * n
    a[0] = b[0]
    a[n-1] = b[n-2]
    for i in range(1, n-1):
        a[i] = b[i-1] - a[i-1]
        if b[i] < a[i]:
            a[i] = b[i]
        if b[i] < a[i+1]:
            a[i+1] = b[i]

    print(sum(a))

if __name__ == '__main__':
    main()

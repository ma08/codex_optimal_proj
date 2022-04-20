

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    b[0] = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            b[i] = b[i-1] + 1
        else:
            b[i] = 1
    c = [0] * n
    c[n-1] = 1
    for i in range(n-2, -1, -1):
        if a[i] < a[i+1]:
            c[i] = c[i+1] + 1
        else:
            c[i] = 1
    ans = 0
    for i in range(n):
        if b[i] + c[i] - 1 > ans:
            ans = b[i] + c[i] - 1
    print(ans)

if __name__ == "__main__":
    main()

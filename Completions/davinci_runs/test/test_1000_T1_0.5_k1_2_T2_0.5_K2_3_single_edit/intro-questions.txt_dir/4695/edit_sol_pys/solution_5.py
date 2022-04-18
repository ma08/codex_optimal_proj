

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if i == 0:
            cnt += b[a[i] - 1]
        else:
            if a[i] - a[i - 1] == 1:
                cnt += b[a[i] - 1] + c[a[i - 1] - 1]
            else:
                cnt += b[a[i] - 1]
    print(cnt)

if __name__ == "__main__":
    main()

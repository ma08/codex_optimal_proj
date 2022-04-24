
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    cnt = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)
    print(ans)

if __name__ == '__main__':
    main()

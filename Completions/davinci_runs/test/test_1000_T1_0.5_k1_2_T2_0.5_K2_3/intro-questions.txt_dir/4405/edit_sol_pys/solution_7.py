

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    cnt = 0
    ans = 0
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans = max(ans, cnt)
            cnt = 1
    print(ans)


if __name__ == '__main__':
    main()
